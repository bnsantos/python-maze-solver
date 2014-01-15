__author__ = 'bruno'
from PIL import Image
import colors
from Queue import Queue


class Maze(object):
    def __init__(self, input_filename, output_filename, start_pos, end_pos):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.start_pos = start_pos
        self.end_pos = end_pos

        self.base_img = None
        self.base_pixels = None
        self.convert_maze_black_white()
        self.width = self.base_img.size[0]
        self.height = self.base_img.size[1]

        x, y = start_pos
        self.set_start_point(x, y)

        x, y = end_pos
        self.set_end_point(x, y)

        self.solved = False
        self.solution_path = []
        self.iterations = 0
        # Save an image every SNAPSHOT_FREQ steps.
        self.snapshot_freq = 100

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
        for i in range(self.width):
            for j in range(self.height):
                pixel = self.base_pixels[i, j]
                if pixel != colors.WHITE and pixel != colors.BLACK:
                    if pixel == colors.BLUE:
                        self.start_pos = (i, j)
                    elif pixel == colors.GREEN:
                        self.end_pos = (i, j)
        if self.start_pos is None or self.end_pos is None:
            print 'ERROR'

    def solve(self):
        #BFS
        queue = Queue()
        # Wrapping the start tuple in a list
        queue.put([self.start_pos])

        self.iterations = 0
        img = 0

        while not queue.empty() and not self.solved:
            path = queue.get()
            last_pixel = path[-1]
            for adjacent in self.get_adjacent(last_pixel):
                x, y = adjacent
                if adjacent == self.end_pos and self.base_pixels[x, y] == colors.GREEN:
                    self.solved = True
                    self.solution_path = path
                    self.base_img.save('{0}/{1:05d}.png'.format('tmp', img))
                    print 'Found solution'
                    break
                if self.base_pixels[x, y] == colors.WHITE:
                    self.base_pixels[x, y] = colors.GRAY
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.put(new_path)

            if self.iterations % self.snapshot_freq == 0:
                self.base_img.save('{0}/{1:05d}.png'.format('tmp', img))
                img += 1
            self.iterations += 1
        if self.solved:
            print 'solution found'
        else:
            print 'did not find solution'

    def get_adjacent(self, point):
        x, y = point
        adjacent = []
        if x > 0:
            adjacent.append((x-1, y))
        if x < self.width-1:
            adjacent.append((x+1, y))
        if y > 0:
            adjacent.append((x, y-1))
        if y < self.height-1:
            adjacent.append((x, y+1))
        return adjacent

    def save_solved(self):
        if self.solved:
            self.draw_path()
            self.base_img.save(self.output_filename)

    def draw_path(self):
        for pixel in self.solution_path:
            x, y = pixel
            self.base_pixels[x, y] = colors.RED

    def convert_maze_black_white(self):
        #Loading first time
        self.base_img = Image.open(self.input_filename)

        # convert image to black and white
        self.base_img = self.base_img.convert('1')
        self.base_img.save(self.input_filename)

        # saving in rgb
        base_img_rgb = Image.new("RGBA", self.base_img.size)
        base_img_rgb.paste(self.base_img)
        base_img_rgb.save(self.input_filename)

        # openning it back in rgba
        self.base_img = Image.open(self.input_filename)
        self.base_pixels = self.base_img.load()