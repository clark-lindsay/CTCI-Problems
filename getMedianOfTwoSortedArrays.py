def getMedianSortedArrays(sequenceA, sequenceB):
    if sequenceA is None or sequenceB is None:
        raise TypeError('requires that neither input argument is None')

    aLength = len(sequenceA)
    bLength = len(sequenceB)

    if aLength > bLength:
        sequenceA, sequenceB = sequenceB, sequenceA
        aLength, bLength = bLength, aLength


    leftHalfLength = (aLength + bLength + 1) // 2

    aMinCount = 0
    aMaxCount = aLength

    while aMinCount <= aMaxCount:
        aCount = aMinCount + ((aMaxCount - aMinCount) // 2)
        bCount = leftHalfLength - aCount

        if aCount > 0 and sequenceA[aCount - 1] > sequenceB[bCount]:
            aMaxCount = aCount - 1
        elif aCount < aLength and sequenceB[bCount - 1] > sequenceA[aCount]:
            aMinCount = aCount + 1
        else:
            lastLeftHandValue = None
            if aCount == 0:
                lastLeftHandValue = sequenceB[bCount - 1]
            elif bCount == 0:
                lastLeftHandValue = sequenceA[aCount - 1]
            else:
                lastLeftHandValue = max(sequenceA[aCount - 1], sequenceB[bCount - 1])

            if isOdd(aLength + bLength):
                return lastLeftHandValue

            firstRightHandValue = None
            if aCount == aLength:
                firstRightHandValue = sequenceB[bCount]
            elif bCount == bLength:
                firstRightHandValue = sequenceA[aCount]
            else:
                firstRightHandValue = min(sequenceA[aCount], sequenceB[bCount])
                
            return (lastLeftHandValue + firstRightHandValue) / 2

        


def isOdd(number):
    return number & 1

