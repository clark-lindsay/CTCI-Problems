def longestSubstringWithoutRepeatChars(s):
    if len(s) <= 1:
        return len(s)
    
    indexOfLastRepeat, longestSoFar = -1, 0
    mostRecentIndex = dict()
    numUniqueChars = len(set(s))
    
    for i, char in enumerate(s):
        if (char in mostRecentIndex and
            mostRecentIndex[char] > indexOfLastRepeat):
            indexOfLastRepeat = mostRecentIndex[char]
        
        mostRecentIndex[char] = i
        longestSoFar = max(longestSoFar, i - indexOfLastRepeat)
        if (longestSoFar == numUniqueChars):
            break
    
    return longestSoFar