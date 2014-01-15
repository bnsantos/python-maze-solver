__author__ = 'bruno'
from maze.maze import Maze

m = Maze('input/simple.png', 'output/solution_simple.png')
#small set up
#m.set_end_point(10, 20)
#m.set_start_point(540, 400)

#m = Maze('input/medium_maze.png', 'output/solution_medium.png')
#medium set up
#m.set_end_point(175, 175)
#m.set_start_point(5, 5)

#m = Maze('input/bigger_maze.png', 'output/solution_bigger.png')
#bigger set up
#m.set_end_point(1990, 605)
#m.set_start_point(5, 530)

m.solve()
m.save_solved()


