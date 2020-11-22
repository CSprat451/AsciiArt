from PIL import Image, ImageDraw, ImageFont
from image_config import ImageConfig
from ascii_art import AsciiArt
import requests
import os
import sys
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
# from flask_cors import CORS

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# CORS(app)

@app.route('/upload')
def upload_image():
    return render_template('upload_image.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def allowed_image_filesize(filesize):
    return int(filesize) <= MAX_IMAGE_FILESIZE


@app.route('/ascii', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        print(request.files)
        if 'file' not in request.files:
            return 'No file part'
            # return redirect(request.url)

        file = request.files['file']
        if not file:
            return 'No file detected'
            # return redirect(request.url)

        if file.filename == '':
            return 'No filename'
            # return redirect(request.url)

        if not allowed_file(file.filename):
            return 'File type not allowed'
        else:
            filename = secure_filename(file.filename)

        if not allowed_image_filesize(sys.getsizeof(file)):
            return 'File size exceeded'

        converted_image = ImageConfig(file)
        image_pixel_matrix = converted_image.get_pixel_matrix()
        ascii_art_image = AsciiArt(image_pixel_matrix)
        ascii_art_image.save_art_image(converted_image.get_new_width(), converted_image.get_new_height(), filename)

        return "File uploaded successfully"
    return "You called get"




# if __name__ == '__main__':