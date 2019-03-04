from collections import deque


class TowerOfHanoi:
    def __init__(self):
        self.diskStack = deque()
    
    def __repr(self):
        return self.diskStack

    def __str__(self):
        return str(list(self.diskStack))

    def moveDisks(self, numDisks, destinationTower, bufferTower):
        if numDisks > 0:
            self.moveDisks(numDisks - 1, bufferTower, destinationTower)
            self.moveTopTo(destinationTower)
            bufferTower.moveDisks(numDisks - 1, destinationTower, self)
    
    def addDisk(self, disk):
        if len(self.diskStack) != 0:
            if self.diskStack[-1] <= disk:
                raise ValueError('Cannot place a disk on a smaller/ equal disk')
        self.diskStack.append(disk)
    
    def moveTopTo(self, otherTower):
        top = self.diskStack.pop()
        otherTower.addDisk(top)

