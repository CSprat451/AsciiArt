from PIL import Image
from ascii_art import AsciiArt
from image_config import ImageConfig
import glob
import os
import re
import cv2
import uuid


class AsciiGif(object):
    def __init__(self, video):
        self.video = cv2.VideoCapture(video)

    def video_to_image(self):
        """
        Extracts each individual frame from a video file and saves as a .jpg to a specified directory.
        Output is a list of the image names.
        """

        # frame
        currentframe = 0
        image_name_list = []

        while True:

            # reading from frame
            ret, frame = self.video.read()

            if ret:
                # if video is still left continue creating images
                name = '../results/image-frame/frame' + str(currentframe) + '.jpg'

                # writing the extracted images
                cv2.imwrite(name, frame)

                image_name_list.append(name)

                # increasing counter so that it will show how many frames are created
                currentframe += 1
            else:
                break

        # Release all space and windows once done
        self.video.release()
        cv2.destroyAllWindows()

        return image_name_list

    def frames_to_ascii(self):
        """
        Converts the image frames extracted from the video file into ascii art images.
        """
        # File path where the image frames were saved
        dir_path = os.path.dirname(os.getcwd())
        image_frames_path = glob.glob(os.path.join(dir_path, 'results', 'image-frame', '*.jpg'), recursive=True)

        # Converts each image into an ascii art image and saves the ascii image file over the original image frame.
        for i in image_frames_path:
            converted_image = ImageConfig(i)
            image_pixel_matrix = converted_image.get_pixel_matrix()
            ascii_art_image = AsciiArt(image_pixel_matrix)
            ascii_art_image.save_art_image(converted_image.get_new_width(), converted_image.get_new_height(), i)

    def ascii_to_gif(self):
        """
        Creates a gif file using image frames and saves the file in a specified directory.
        Output is a gif file.
        """
        # Create unique filename for every gif
        unique_filename = (str(uuid.uuid4()) + ".gif")

        # Set up the file path to save the gif with a unique filename
        dir_path = os.path.dirname(os.getcwd())
        rel_path = os.path.join(dir_path, 'results', 'ascii-gif', unique_filename)

        # Where to find the saved ascii image frames
        frames = []
        images = glob.glob(os.path.join(dir_path, 'results', 'image-frame', '*.jpg'), recursive=True)

        # Make dictionary using the frame number (key) and full path to the image frame (value)
        sorted_images = {}

        for i in images:
            image_number = re.split(r'(\d+)', i)
            sorted_images[int(image_number[1])] = i

        # Sort the frame numbers and add the image frames to the gif in numerical order
        for key in sorted(sorted_images.keys()):
            new_frame = Image.open(sorted_images[key])
            frames.append(new_frame)

        # Saves the gif to the directed file above
        print(frames)
        frames[0].save(rel_path, format='GIF', append_images=frames[0:], save_all=True, duration=100, loop=0)
        return unique_filename


# ascii_gif = AsciiGif('sample_Trim.mp4')
# ascii_gif.video_to_image()
# ascii_gif.frames_to_ascii()
# ascii_gif.ascii_to_gif()
