def englishInt(integer):
    intString = str(integer)
    if len(intString) == 1:
        return _singleCharacterEnglishInt(intString).rstrip()
    resultString = ''
    postFixList = ['', 'Thousand, ', 'Million, ', 'Billion, ', 'Trillion, ', 'Quadrillion, ', 'Quintillion ']
    lastBreakIndex = 0
    for i in range(len(intString)):
        remainingLength = len(intString[i:])
        if (remainingLength % 3 == 0) and i != 0:
            resultString += _threeDigitEnglishInt(intString[lastBreakIndex:i])
            resultString += postFixList[remainingLength // 3]
            lastBreakIndex = i
    return (resultString + _threeDigitEnglishInt(intString[lastBreakIndex:])).rstrip()

def _threeDigitEnglishInt(integerString):
    result = ''
    startIndex = 0
    if len(integerString) == 3 and integerString[0] != '0':
        result += _oneDigitEnglishInt(integerString[startIndex]) + 'Hundred '
        startIndex += 1
    return result + _twoDigitEnglishInt(integerString[startIndex:])

def _twoDigitEnglishInt(integerString):
    prefixLookup = {'2': 'Twenty ', '3': 'Thirty ',
                    '4': 'Forty ', '5': 'Fifty ',
                    '6': 'Sixty ', '7': 'Seventy ',
                    '8': 'Eighty ', '9': 'Ninety '}
    if len(integerString) == 2 and integerString[0] == '1':
        return _teenEnglishInt(integerString)
    elif len(integerString) == 1 or integerString[0] == '0':
        return _oneDigitEnglishInt(integerString[-1])
    else:
        return prefixLookup[integerString[0]] + _oneDigitEnglishInt(integerString[-1])

def _teenEnglishInt(integerString):
    teenLookup = {'11': 'Eleven ', '12': 'Twelve ',
                    '13': 'Thirteen ', '14': 'Fourteen ',
                    '15': 'Fifteen ', '16': 'Sixteen ',
                    '17': 'Seventeen ', '18': 'Eighteen ',
                    '19': 'Nineteen '}
    return teenLookup[integerString]

def _singleCharacterEnglishInt(integerString):
    if integerString == '0':
        return 'Zero'
    else:
        return _oneDigitEnglishInt(integerString)

def _oneDigitEnglishInt(integerString):
    singleDigitLookup = {'1': 'One ', '2': 'Two ',
                        '3': 'Three ', '4': 'Four ',
                        '5': 'Five ', '6': 'Six ',
                        '7': 'Seven ', '8': 'Eight ',
                        '9': 'Nine ', '0': ''}
    return singleDigitLookup[integerString]

