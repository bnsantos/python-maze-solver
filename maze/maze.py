__author__ = 'bruno'
from PIL import Image


class Maze(object):
    def __init__(self, filename):
        self.base_img = Image.open(filename)
        self.base_pixels = self.base_img.load()
        self.start_pos = None
        self.end_pos = None
        self.solved = False

    def is_solved(self):
        return self.solved

    def find_start_and_end_point(self):
        pass
