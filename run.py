__author__ = 'bruno'
from maze.maze import Maze

m = Maze('input/final_maze.png', 'output/solution_final.png', (5, 460), (230, 235))
#final set up


#small
#m = Maze('input/simple.png', 'output/solution_simple.png', (540, 400), (10, 20))

#medium
#m = Maze('input/medium_maze.png', 'output/solution_medium.png', (5, 5), (175, 175))

#bigger set up
#m = Maze('input/bigger_maze.png', 'output/solution_bigger.png', (5, 530), (1990, 605))

m.solve()
m.save_solved()


