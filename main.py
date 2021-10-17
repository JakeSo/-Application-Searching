import gridops
import informed
import local
import nqueens
import uninformed

grid = gridops.readGrid('grid.txt')
start, goal = gridops.genStartGoal(grid)
uninformed.uninformedsearch(start, goal, grid)
path = [x.location for x in uninformed.bfspath]

informed.A_star(start, goal, grid)
informed.greedy(start, goal, grid)

local.runTests()
