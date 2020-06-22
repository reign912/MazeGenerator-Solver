from maze import *
import time

m = Maze()
start = time.time()
m.create(50, 50, Maze.Create.PRIM) #PRIM/KRUSKAL can be used here and also can change 
end = time.time()                  # no. of rows and column
print("Time taken to create maze",end - start)
m.save_maze()

start = time.time()
m.solve((0, 0), (49, 49), Maze.Solve.DEPTH) #DEPTH/ BREADTH can be used here
end = time.time()
print("Time taken to solve maze",end - start)
m.save_solution()
