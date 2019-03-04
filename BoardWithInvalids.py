class BoardWithInvalids:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.grid = [[_] * self.width for i in range(self.height)]
        self.invalidLocations = set()

    def __repr__(self):
        result = ''
        for row in self.grid:
            result += str(row) + '\n'
        return result
    
    def isValidLocation(self, location):
        row, column = location
        if (row >= 0 and row < self.height) and (column >= 0 and column < self.width):
            return location not in self.invalidLocations
        else:
            return False

    def setInvalid(self, location):
        self.invalidLocations.add(location)
    
