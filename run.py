__author__ = 'bruno'
from maze.maze import Maze

m = Maze('input/simple.png', 'output/solution.png')
m.solve()
m.save_solved()
#m.set_end_point(10, 20)
#m.set_start_point(540, 400)

