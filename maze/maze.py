__author__ = 'bruno'
from PIL import Image
import colors


class Maze(object):
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.base_img = Image.open(self.input_filename)
        self.base_pixels = self.base_img.load()
        self.start_pos = None
        self.end_pos = None
        self.solved = False
        self.find_start_and_end_point()

    def is_solved(self):
        return self.solved

    def set_end_point(self, x, y):
        self.set_point_color(x, y, colors.GREEN)

    def set_start_point(self, x, y):
        self.set_point_color(x, y, colors.BLUE)

    def set_point_color(self, x, y, color):
        self.base_pixels[x, y] = color
        #overriding picture
        self.base_img.save(self.input_filename)

    def find_start_and_end_point(self):
        width = self.base_img.size[0]
        height = self.base_img.size[1]

        for i in range(width):
            for j in range(height):
                pixel = self.base_pixels[i, j]
                if pixel != colors.WHITE and pixel != colors.BLACK:
                    if pixel == colors.BLUE:
                        self.start_pos = (i, j)
                    elif pixel == colors.GREEN:
                        self.end_pos = (i, j)
        if self.start_pos is None or self.end_pos is None:
            print 'ERROR'