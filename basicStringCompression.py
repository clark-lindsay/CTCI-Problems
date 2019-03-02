''' would benefit from a stringBuilder... how does Python's string concatenation work under the hood?'''
def basicStringCompression(string):
    if len(string) <= 1:
        return string
    currentChar = string[0]
    currentCharCount = 1
    resultString = ''
    for char in string[1:]:
        if char != currentChar:
            resultString += currentChar + str(currentCharCount)
            currentChar, currentCharCount = char, 1
        else:
            currentCharCount += 1
    resultString += currentChar + str(currentCharCount)
    if len(string) <= len(resultString):
        return string
    else:
        return resultString