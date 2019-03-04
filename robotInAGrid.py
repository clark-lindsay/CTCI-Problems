from BoardWithInvalids import *
from collections import deque
''' This is untested! '''
def findPath(board):
    currentLocation = (0, 0)
    pathStack = deque()
    pathStack.append(currentLocation)
    decisionStack = deque()
    if isStuck(board, currentLocation):
        return list()
    while(not pathStack.empty()):
        currentRow, currentColumn = currentLocation
        if not isStuck(board, currentLocation):
            if canGoDown(board, currentLocation):
                decisionStack.append((currentRow + 1, currentColumn))
            if canGoRight(board, location):
                decisionStack.append((currentRow, currentColumn + 1))
        else:
            pathStack.pop()
        currentLocation = decisionStack.pop()
        pathStack.append(currentLocation)
    return list(pathStack)

def isStuck(board, location):
    row, column = location
    return board.isValidLocation((row + 1, column)) and board.isValidLocation((row, column + 1))

def canGoDown(board, location):
    row, column = location
    return board.isValidLocation((row + 1, column))

def canGoRight(board, location):
    row, column = location
    return board.isValidLocation((row, column + 1))