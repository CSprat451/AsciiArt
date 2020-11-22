import numpy as np
from PIL import Image


class ImageConfig(object):
    def __init__(self, image):
        self.image = Image.open(image)
        self.original_width, self.original_height = self.image.size
        self.new_width, self.new_height = 0, 0

    def convert_grayscale(self):
        return self.image.convert("L")

    def resize_image(self, width=200):
        """
        Resizes image and will keep the aspect ratio.
        """
        self.new_width = width
        aspect_ratio = self.original_height/float(self.original_width)
        self.new_height = int(aspect_ratio * self.new_width)

        resized_image = self.image.resize((self.new_width, self.new_height), Image.BILINEAR)
        return resized_image

    def get_new_width(self):
        return self.new_width

    def get_new_height(self):
        return self.new_height

    def get_pixel_matrix(self):
        """
        Converts and image into tuples with the R, G, B code in each tuple.
        returns: a 2D array of R, G, B tuples
        """
        resized_image = self.resize_image()
        pixel_matrix = np.asarray(resized_image)

        return pixel_matrix
