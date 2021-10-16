import copy

# The grid values must be separated by spaces, e.g.
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# Returns a 2D list of integers
def readGrid(filename):
    #print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])

    f.close()
    #print 'Exiting readGrid'
    return grid


# Writes a 2D list of 1s and 0s with spaces in between each character
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
def outputGrid(grid, start, goal, nodepath):
    #print('In outputGrid')
    filenameStr = 'path.txt'

    path = [x.location for x in nodepath]
    # Open filename
    f = open(filenameStr, 'w')

    gridcopy = copy.deepcopy(grid)
    # Mark the start and goal points
    gridcopy[start[0]][start[1]] = 'S'
    gridcopy[goal[0]][goal[1]] = 'G'

    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path) - 1:
            gridcopy[p[0]][p[1]] = '*'

    # Write the gridcopy to a file
    for r, row in enumerate(gridcopy):
        for c, col in enumerate(row):

            # Don't add a ' ' at the end of a line
            if c < len(row) - 1:
                f.write(str(col) + ' ')
            else:
                f.write(str(col))

        # Don't add a '\n' after the last line
        if r < len(gridcopy) - 1:
            f.write("\n")

    # Close file
    f.close()
    #print('Exiting outputGrid')
