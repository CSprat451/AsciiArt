from PIL import Image, ImageDraw, ImageFont

ASCII_CHARACTERS = "`.^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_BRIGHTNESS = 256
FONT = "consolab.ttf"
FONT_SIZE = 20


class AsciiArt(object):
    def __init__(self, pixel_matrix):
        self.pixel_matrix = pixel_matrix
        self.intensity_matrix = self.get_intensity_matrix()
        self.ascii_matrix = self.get_ascii_matrix()

    def get_intensity_matrix(self):
        intensity_matrix = []
        for row in self.pixel_matrix:
            intensity_row = []
            for p in row:
                intensity = (0.21 * p[0]) + (0.72 * p[1]) + (0.07 * p[2])
                intensity_row.append(intensity)
            intensity_matrix.append(intensity_row)

        return intensity_matrix

    def normalize_intensity_matrix(self):
        normalized_intensity_matrix = []
        max_pixel = max(map(max, self.intensity_matrix))
        min_pixel = min(map(min, self.intensity_matrix))
        for row in self.intensity_matrix:
            rescaled_row = []
            for p in row:
                r = MAX_PIXEL_BRIGHTNESS * (p - min_pixel) / float(max_pixel - min_pixel)
                rescaled_row.append(r)
            normalized_intensity_matrix.append(rescaled_row)

        return normalized_intensity_matrix

    def get_ascii_matrix(self):
        """
        Converts the pixel_brightness number to a corresponding ascii character.
        returns: a list of ascii characters
        """
        ascii_matrix = []

        for row in self.normalize_intensity_matrix():
            ascii_row = []
            for p in row:
                ascii_row.append(ASCII_CHARACTERS[int(p/MAX_PIXEL_BRIGHTNESS * len(ASCII_CHARACTERS)) - 1])
            ascii_matrix.append(ascii_row)
        return ascii_matrix

    def print_ascii_matrix(self):
        for row in self.ascii_matrix:
            line = [p + p for p in row]
            print("".join(line))

    def save_art_text(self):
        ascii_art_file = open("ascii-art.txt", "w")
        for row in self.ascii_matrix:
            line = [p + p for p in row]
            ascii_art_file.write("".join(line) + "\n")
        ascii_art_file.close()

    def save_art_image(self, new_width, new_height, filename):
        ascii_image = Image.new('L', (new_width*24, new_height*24), 0)
        draw = ImageDraw.Draw(ascii_image)
        font = ImageFont.truetype(FONT, FONT_SIZE)

        pt2px = lambda pt: int(round(pt * 96.0 / 72))
        max_height = pt2px(font.getsize(ASCII_CHARACTERS)[1])
        vertical_position = 5
        horizontal_position = 5
        line_spacing = int(round(max_height * 0.7))

        for row in self.ascii_matrix:
            line = [p + p for p in row]
            draw.text((horizontal_position, vertical_position), "".join(line), 255, font=font)
            vertical_position += line_spacing

        ascii_image_resize = ascii_image.resize((new_width*8, new_height*8), Image.ANTIALIAS)
        ascii_image_resize.show()
        ascii_image_resize.save(filename + "-ascii.jpg")
