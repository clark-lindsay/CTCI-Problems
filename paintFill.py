class PixelGrid:
    def __init__(self, width=100, height=100):
        self.grid = [[Pixel()] * width for i in range(height)]

    def paintFill(self, clickPoint, color):
        if (not self._isValidPoint(*clickPoint)):
            raise ValueError('Coordinates given are not within the range of the grid')
        _bloom(clickPoint, self.grid[clickPoint], color)

    def _bloom(self, coordinates, originalColor, newColor):
        if grid[coordinates] == originalColor:
            grid[coordinates] = newColor
        row, column = coordinates
        self._bloom((row, column + 1), originalColor, newColor)
        self._bloom((row, column - 1), originalColor, newColor)
        self._bloom((row + 1, column), originalColor, newColor)
        self._bloom((row - 1, column - 1), originalColor, newColor)


        
    def _isValidPoint(self, x, y):
        if x >= 0 and x < 256 and y >= 0 and y < 256:
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
     
    def __str__(self):
        return 'R:%s, G:%s, B%s'.format(self.r, self.g, self.b)
