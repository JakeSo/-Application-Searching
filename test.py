# Tests

import matplotlib
from matplotlib import colors
import matplot.pyplot as plt
import numpy as np
import random

def genStartGoal(grid):

	sRow = random.randint(0, len(grid)-1)
	sCol = random.randint(0, len(grid[0])-1)

	while grid[sRow][sCol] == 0:
		sRow = random.randint(0, len(grid)-1)
		sCol = random.randint(0, len(grid[0])-1)

		
	gRow = random.randint(0, len(grid)-1)
	gCol = random.randint(0, len(grid[0])-1)

	while grid[gRow][gCol] == 0:
		gRow = random.randint(0, len(grid)-1)
		gCol = random.randint(0, len(grid[0])-1)

	return [sRow, sCol], [gRow, gCol]

def genGrid(size, max_cost=9):
	""" Generates a grid with random values in range [0,max_cost] where 0s represent obstacle cells and 1-max_cost represent the step cost to move onto the cell from any neighbor.

	Parameters:
		size (int): The number of rows and columns to useh
		max_cost (int): The max step cost to move onto a celll in the grid
		
	Returns:
		2D list: The randomly generated grid
	"""
	
	num_rows = size
	num_cols = size
	
	grid = [[0]*num_cols for i in range(0,num_rows)]
	
	ob_cost = 0
	ob_prob = 0.2
	
	for i_r in range(0,num_rows):
			for i_c in range(0,num_cols):
					
					# Default to obstacle cost
					cost = ob_cost
					
					# Chance to be an obstacle
					chance = random.random()
					if chance > ob_prob:
							# Generate a random cost for the location
							cost = random.randint(1,max_cost)
							
					grid[i_r][i_c] = cost

	return grid


def labelTile(grid, r, c, ax, text):
	""" Puts a character onto a grid cell, and changes text color based on cell color
		
	Parameters:
		grid (2D list): The grid to visualize
		r (int): The row of the cell to label
		c (int): The column of the cell to label
		text (string): The text to put onto the grid cell
		
	Returns:
		None
	"""
	if grid[r][c] <= 3:
		ax.text(c, r, text, color="white", ha='center', va='center' )
	else:
		ax.text(c, r, text, color="black", ha='center', va='center' )



def visualizeGrid(grid, path=False, block=False, max_cost=9):
	""" Displays the grid as a grayscale image where each cell is shaded based on the step cost to move onto it. 
			
	Parameters:
			grid (2D list): The grid to visualize
			path (2D list): The path to visualize.
			block (bool): True if pyplot.show should block program flow until the window is closed
			max_cost(int): Maximum step cost to move onto any cell in the grid
			
	Returns:
			None
	"""
	tempGrid = []

	# Flip the values so that darker means larger cost
	for r in grid:
			row = []
			for col in r:
					if col != 0:
						col = (max_cost+1) - col
					row.append(col)
			tempGrid.append(row)
			
					
	# Create colors
	cmap = matplotlib.cm.gray
	norm = colors.Normalize(vmin=0,vmax=max_cost)
	
	# Call imshow
	fig, ax = plt.subplots()
	ax.imshow(tempGrid, interpolation="none", cmap=cmap, norm=norm)

	# Put a 'p' character for each path position
	for i,loc in enumerate(path):
		if i == 0:
			labelTile(tempGrid, loc[1], loc[0], ax, "S")
		elif i == len(path)-1:
			labelTile(tempGrid, loc[1], loc[0], ax, "G")
		else:
			labelTile(tempGrid, loc[1], loc[0], ax, "p")

	
	if len(grid) <= 20:
		# Set ticks
		tickInc = 1
	else:
		tickInc = int(len(grid) / 10)

	ax.set_xticks(np.arange(0, len(grid)+1, tickInc))
	ax.set_yticks(np.arange(0, len(grid[0])+1, tickInc))
	ax.set_xticklabels(np.arange(0,len(grid)+1, tickInc))
	ax.set_yticklabels(np.arange(0,len(grid[0])+1, tickInc))

	plt.show(block=False)