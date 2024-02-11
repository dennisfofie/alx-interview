#!/usr/bin/python3
"""
island perimeter algorithm
"""

def island_perimeter(grid):
    """
    Description - compute the perimeter of island
     @Argument:
            grid - island in 2-dimensional array
    Return: perimeter of the island
    """
    if not grid:
        return 0

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
