import numpy as np
from PIL import Image


class ImageConfig(object):
    def __init__(self, image):
        self.image = Image.open(image)
        self.original_width, self.original_height = self.image.size
        self.new_width, self.new_height = 0, 0

    def convert_grayscale(self):
        """
        Converts colored R, G, B image to a grayscale image.
        """
        return self.image.convert("L")

    def resize_image(self, width=200):
        """
        Resizes image to a width of 200 pixels and will keep the aspect ratio of the original image.
        """
        self.new_width = width
        aspect_ratio = self.original_height/float(self.original_width)
        self.new_height = int(aspect_ratio * self.new_width)

        resized_image = self.image.resize((self.new_width, self.new_height), Image.BILINEAR)
        return resized_image

    def get_new_width(self):
        """
        Returns the new width of the resized image.
        """
        return self.new_width

    def get_new_height(self):
        """
        Returns the new height of the resized image.
        """
        return self.new_height

    def get_pixel_matrix(self):
        """
        Converts an image into tuples with the R, G, B value in each tuple.
        returns: a 2D array of R, G, B tuples
        """
        resized_image = self.resize_image()
        pixel_matrix = np.asarray(resized_image)

        return pixel_matrix


