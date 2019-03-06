def numberOfSteps(binaryString):
    if binaryString == '0':
        return 0
    if binaryString == '1':
        return 1
        
    binaryString = binaryString[::-1]
    binaryString = binaryString.rstrip('0')
    numSteps = 0

    for char in binaryString[:len(binaryString) - 1]:
        if char == '1':
            numSteps += 2
        else:
            numSteps += 1
    if binaryString[-1] == '1':
        numSteps += 1
    return numSteps