import math
import heapq

import gridops

sloc = []
gloc = []

class Node():
    """docstring forNode."""

    def __init__(self, loc, g, parent):
        self.location = loc
        self.parent = parent
        if not isinstance(parent, Node):
            self.g = g
        else:
            self.g = parent.g + g
        self.h = heuristic(loc)
        self.f = self.h + self.g

    def __lt__(self, other):

        return self.f < other.f


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


def expandNode(c, grid, closedList, openList, greedy = False):
    x = getNeighbors(c.location, grid)
    for i in x:
        b = False
        if (openList.get(i) == 1):
            b = True
            break
        for j in closedList:
            if (i == j.location):
                b = True
                break
        if (b == False):
            if greedy:
                neighbor = Node(i, 0, c)
            else:
                neighbor = Node(i, grid[i[0]][i[1]], c)
            openList.push(neighbor)
    return openList

def heuristic(location):
    return math.sqrt((location[0] - gloc[0]) ** 2 + (location[1] - gloc[1]) ** 2)


# The grid values must be separated by spaces, e.g.
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# Returns a 2D list of integers
def readGrid(filename):
    # print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])

    f.close()
    # print 'Exiting readGrid'
    return grid


# Writes a 2D list of 1s and 0s with spaces in between each character
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
def outputGrid(grid, start, goal, path):
    # print('In outputGrid')
    filenameStr = 'path.txt'

    # Open filename
    f = open(filenameStr, 'w')

    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path) - 1:
            grid[p[0]][p[1]] = '*'

    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):

            # Don't add a ' ' at the end of a line
            if c < len(row) - 1:
                f.write(str(col) + ' ')
            else:
                f.write(str(col))

        # Don't add a '\n' after the last line
        if r < len(grid) - 1:
            f.write("\n")

    # Close file
    f.close()
    # print('Exiting outputGrid')


class pqueue:
    def __init__(self):
        self.queue = []

    def push(self, node):
        heapq.heappush(self.queue, node)

    def pop(self):
        return heapq.heappop(self.queue)

    def get(self, loc):
        for n in self.queue:
            if loc == n.location:
                return 1
        return -1


def A_star(initial, goal, grid):
    print("A*:")
    olist = pqueue()
    clist = []
    path = []
    global gloc
    global sloc
    gloc = goal
    sloc = initial

    expanded = 0

    start = Node(initial, grid[initial[0]][initial[1]], None)

    olist.push(start)

    while (len(olist.queue) != 0):
        current = olist.pop()
        clist.append(current)
        if current.location == goal:
            cost = current.g
            while current != None:
                path.append(current)
                current = current.parent
            path.reverse()
            gridops.outputGrid(grid, start.location, goal, path)
            f = open('path.txt', 'r')
            print(f.read())
            print("Path cost = " + str(cost))
            print("Expanded Nodes = " + str(expanded) + "\n")
            break
        else:
            olist = expandNode(current, grid, clist, olist)
            expanded += 1

def greedy(initial, goal, grid):
    print("Greedy:")
    olist = pqueue()
    clist = []
    path = []
    global gloc
    global sloc
    gloc = goal
    sloc = initial

    expanded = 0

    start = Node(initial, 0, None)

    olist.push(start)

    while len(olist.queue) != 0:
        current = olist.pop()
        clist.append(current)
        if current.location == goal:
            cost = 0
            while current != None:
                path.append(current)
                loc = current.location
                cost += grid[loc[0]][loc[1]]
                current = current.parent
            path.reverse()
            gridops.outputGrid(grid, start.location, goal, path)
            f = open('path.txt', 'r')
            print(f.read())
            print("Path cost = " + str(cost))
            print("Expanded Nodes = " + str(expanded))
            break
        else:
            olist = expandNode(current, grid, clist, olist, True)
            expanded += 1


# node=Node([3,2], None)
# openList=expandNode(node, grid, closedList, openList)
# for i in openList:
#  print(i.value, end = " ")

# print('\n')
# node=Node([9,9], None)
# openList=expandNode(node, grid, closedList, openList)
# for i in openList:
#  print(i.value, end = " ")
# print('\n')

# node=Node([2,3], None)
# openList=expandNode(node, grid, closedList, openList)
# for i in openList:
#  print(i.value, end = " ")