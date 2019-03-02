def isStringRotation(stringOne, stringTwo):
    if len(stringOne) != len(stringTwo) or len(stringOne) == 0:
        return False
    stringTwo *= 2
    return stringOne in stringTwo
