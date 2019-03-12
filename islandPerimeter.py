class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # a single land tile adds 4 - the number of land tiles it is touching to the perimeter
        #only need to scan until you no longer encounter land tiles in a row
        totalIslandPerimeter = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if isLand(row, column, grid):
                    totalIslandPerimeter += getLandPerimeter(row, column, grid)
        return totalIslandPerimeter


def isValid(row, column, grid):
    if ((row >= 0 and row < len(grid)) and 
    (column >= 0  and column < len(grid[0]))):
        return True
    else:
        return False

def isLand(row, column, grid):
    if isValid(row, column, grid):
        return grid[row][column] == 1
    else:
        return False

def getLandPerimeter(row, column, grid):
    if (not isValid(row, column, grid) and not isLand(row, column, grid)):
        raise ValueError('The self passed to "getLandPerimeter" must be valid, and refer to a land tile')
    perimeter = 0
    left = row, column -1
    right = row, column + 1
    up = row - 1, column
    down = row + 1, column
    adjacentTiles = [left, right, up, down]
    for tile in adjacentTiles:
        if not isLand(*tile, grid):
            perimeter += 1
    return perimeter
    