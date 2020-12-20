import glob
from PIL import Image
import os
import re
import uuid


def ascii_to_gif():
    """
    Creates a gif file using image frames and saves the file in a specified directory.
    Output is a gif file.
    """
    # Create unique filename for every gif
    unique_filename = (str(uuid.uuid4()) + ".gif")

    # Set up the file path to save the gif with a unique filename
    dir_path = os.path.dirname(os.getcwd())
    rel_path = os.path.join(dir_path, 'results', 'ascii-gif', unique_filename)

    # Where to find the saved image frames
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
        # print(frames)
    frames[0].save(rel_path, format='GIF', append_images=frames[0:], save_all=True, duration=100, loop=0)
    return unique_filename


ascii_to_gif()
