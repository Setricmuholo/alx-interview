#!/usr/bin/python3

"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """

    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    # Define directions for checking adjacent cells (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Each land cell contributes 4 to the perimeter

                # Check adjacent cells
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc

                    # If the adjacent cell is also land, subtract 1 from the perimeter
                    if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == 1:

                        perimeter -= 1

    return perimeter
