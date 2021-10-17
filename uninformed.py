from matplotlib import pyplot as plt

import gridops

bfspath = []
dfspath = []


class Node():
    """docstring forNode."""

    def __init__(self, loc, g, parent):
        self.location = loc
        if (parent != None):
            self.g = g + parent.g
        else:
            self.g = g
        self.parent = parent

    def __lt__(self, other):
        return self.g < other.g


def getNeighbors(location, grid):
    list = []
    r = location[0]
    c = location[1]
    # Above
    if (r - 1 >= 0 and grid[r - 1][c + 0] != 0):
        list.append([r - 1, c + 0])
    # Right
    if (c + 1 < len(grid) and grid[r + 0][c + 1] != 0):
        list.append([r + 0, c + 1])
    # Below
    if (r + 1 < len(grid) and grid[r + 1][c + 0] != 0):
        list.append([r + 1, c + 0])
    # Left
    if ((c - 1) >= 0 and grid[r + 0][c - 1] != 0):
        list.append([r + 0, c - 1])
    return list


def expandNode(c, grid, closedList, openList):
    x = getNeighbors(c.location, grid)
    for i in x:
        b = False
        for j in openList:
            if (i == j.location):
                b = True
                break
        for j in closedList:
            if (i == j.location):
                b = True
                break
        if (b == False):
            neighbor = Node(i, grid[i[0]][i[1]], c)
            openList.append(neighbor)
    return openList


def uninformedsearch(start, goal, grid):
    # Breadth-First Search
    print("Breadth-First Search: ")
    olist = []
    clist = []
    global bfspath
    expanded = 0

    start = Node(start, grid[start[0]][start[1]], None)

    olist.append(start)

    while (len(olist) > 0):
        current = olist.pop(0)
        clist.append(current)

        if (current.location == goal):
            bfspath.clear()
            cost = current.g
            while (current != None):
                bfspath.append(current)
                current = current.parent
            bfspath.reverse()
            gridops.outputGrid(grid, start.location, goal, bfspath)
            f = open('path.txt', 'r')
            print(f.read())
            print("Path cost = " + str(cost))
            print("Expanded Nodes = " + str(expanded) + "\n")
            break

        olist = expandNode(current, grid, clist, olist)
        expanded += 1

    print("Depth-First Search: ")
    olist.clear()
    clist.clear()
    dfspath.clear()
    expanded = 0

    olist.append(start)

    while (len(olist) > 0):
        current = olist.pop()
        clist.append(current)

        if (current.location == goal):
            cost = current.g
            while (current != None):
                dfspath.append(current)
                current = current.parent
            dfspath.reverse()
            gridops.outputGrid(grid, start.location, goal, dfspath)
            f = open('path.txt', 'r')
            print(f.read())
            print("Path cost = " + str(cost))
            print("Expanded Nodes = " + str(expanded) + "\n")
            break

        olist = expandNode(current, grid, clist, olist)
        expanded += 1


def runTests(displayGrids=False):
    """ Runs a series of planning queries on randomly generated maps, map sizes, and start and goal pairs
		
		Parameters:
				displayGrid (bool): True will use matplotlib to visualize the grids
				
		Returns:
				None
	"""
    numExpanded = []
    totalGridSize = 100
    gridSizes = [i for i in range(10, totalGridSize, 5)]

    numTests = 100

    # For each grid size
    for gs in gridSizes:
        numEx = []
        # Do X tests where X=numTests
        for i in range(0, numTests):

            # Get random grid, start, and goal
            grid = gridops.genGrid(gs)
            start, goal = gridops.genStartGoal(grid)

            # Call algorithm
            [p, numExp] = uninformedsearch(start, goal, grid)
            # Display grids if desired
            if i < 2 and gs <= 50 and displayGrids:
                gridops.visualizeGrid(grid, p)

            # Store data for single run
            numEx.append(numExp)

        # Store data for grid size
        numExpanded.append(numEx)

    # Get average of expanded nodes for each grid size
    neAvg = []
    for i, n in enumerate(numExpanded):
        print("Grid size: %s" % gridSizes[i])
        avg = 0
        for e in n:
            avg += e
        avg = avg / len(n)
        neAvg.append(avg)
        print("Average number of expanded nodes: %s" % avg)

    # Display bar graph for expanded node data
    plt.clf()
    plt.bar(gridSizes, neAvg)
    plt.show()
