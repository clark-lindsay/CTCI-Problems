class PixelGrid:
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        self.grid = [[Pixel()] * width for i in range(height)]

    def __str__(self):
        result = ''
        for row in self.grid:
            result += str(row) + '\n'
        return result

    def paintFill(self, clickPoint, color):
        row, column = clickPoint
        if (not self._isValidPoint(row, column)):
            raise ValueError('Coordinates given are not within the range of the grid')
        self._bloom(clickPoint, self.grid[row][column], color)

    def _bloom(self, coordinates, originalColor, newColor):
        row, column = coordinates
        if (not self._isValidPoint(row, column)):
            return
        if self.grid[row][column] == originalColor:
            self.grid[row][column] = newColor
            self._bloom((row, column + 1), originalColor, newColor)
            self._bloom((row, column - 1), originalColor, newColor)
            self._bloom((row + 1, column), originalColor, newColor)
            self._bloom((row - 1, column), originalColor, newColor)


        
    def _isValidPoint(self, row, column):
        if row >= 0 and row < self.height and column >= 0 and column < self.width:
            return True
        else:
            return False

class Pixel:
    def __init__(self, r=0, g=0, b=0):
        if (r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255):
            raise(ValueError('Color intensity outside of bounds [0-255]'))
        self.r = r
        self.g = g
        self.b = b
     
    def __repr__(self):
        return 'R:{}, G:{}, B{}'.format(self.r, self.g, self.b)

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b
