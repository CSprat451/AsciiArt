from image_config import ImageConfig
from ascii_art import AsciiArt
from ascii_gif import AsciiGif
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
import sys
import uuid
import os

home_dir = os.path.expanduser('~')
UPLOAD_FOLDER = os.path.join(home_dir, 'PycharmProjects', 'Robert-Heaton-Projects', 'ASCII Art', 'src')
ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg']
ALLOWED_VIDEO_EXTENSIONS = ['mp4']
MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024

app = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_image_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS


def allowed_video_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_VIDEO_EXTENSIONS


def allowed_image_filesize(filesize):
    return int(filesize) <= MAX_IMAGE_FILESIZE


@app.route('/ascii', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        print(request.files)
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']
        if not file:
            return 'No file detected'

        if file.filename == '':
            return 'No filename'

        if not allowed_image_filesize(sys.getsizeof(file)):
            return 'File size exceeded'

        if allowed_image_file(file.filename):
            converted_image = ImageConfig(file)
            image_pixel_matrix = converted_image.get_pixel_matrix()
            ascii_art_image = AsciiArt(image_pixel_matrix)
            saved_image_name = ascii_art_image.save_art_image(converted_image.get_new_width(),
                                                              converted_image.get_new_height(),
                                                              str(uuid.uuid4()) + ".jpg")
            return "http://localhost:5000/ascii/image/" + saved_image_name.strip('.jpg')

        elif allowed_video_file(file.filename):
            print(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            ascii_gif = AsciiGif(file.filename)
            ascii_gif.video_to_image()
            ascii_gif.frames_to_ascii()
            saved_gif_name = ascii_gif.ascii_to_gif()
            return "http://localhost:5000/ascii/gif/" + saved_gif_name.strip('.gif')

        else:
            return 'File type not allowed'

    return "You called get"


@app.route('/ascii/image/<image_id>', methods=['GET'])
def get_image(image_id):
    return send_file('../results/image-frame' + image_id + ".jpg")


@app.route('/ascii/gif/<gif_id>', methods=['GET'])
def get_gif(gif_id):
    return send_file('../results/ascii-gif' + gif_id + ".gif")

