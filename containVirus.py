class  QuarantineModel:
    def __init__(self, grid):
        self.grid = grid

    def __repr__(self):
        return self.grid
    
    def _findInfectedRegions(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    pass
class InfectedRegion:
    def __init__(self, coordinateSequence):
        self.tiles = coordinateSequence
        #TODO calculate perimeter and area of the given coordinate sequence
        self.contained = False
    
    def __repr__(self):
        return self.tiles
    
    def grow(self):
        pass
        #TODO define the function to grow an infected region