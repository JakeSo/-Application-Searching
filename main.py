import uninformed
import gridops
import test

grid = gridops.readGrid('grid.txt')
startgoal = test.genStartGoal(grid)
uninformed.uninformedsearch(startgoal[0], startgoal[1], grid)


