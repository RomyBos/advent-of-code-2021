inputfile = open('day-10/day10_input.txt', 'r')
# inputfile = open('day-10/day10_input_ex.txt', 'r')

OPENING_CHARS = ['(', '[', '{', '<']
CLOSING_CHARS = [')', ']', '}', '>']
CHARSDICT = {'(': ')', '[': ']', '{': '}', '<': '>'}
CHARSSCOREDICT = {')': 3, ']': 57, '}': 1197, '>': 25137}
CHARSSCOREDICTPART2 = {')': 1, ']': 2, '}': 3, '>': 4}

def getIllegalCharacters(inputfile):
    illegalCharsList = []
    closingCharsList = []
    lines = inputfile.readlines()
    for i in range(len(lines) -1, -1, -1):
        openCharStack = []
        illegalCharsListLine = []
        closingCharsListLine = []
        expectedClosingChar = ''
        line = list(lines[i].strip())
        for char in line:
            if char in OPENING_CHARS:
                openCharStack.append(char)
                expectedClosingChar = CHARSDICT[openCharStack[-1]]
            elif char != expectedClosingChar:
                illegalCharsListLine.append(char)
                openCharStack.pop()
                if openCharStack:
                    expectedClosingChar = CHARSDICT[openCharStack[-1]]
            else:
                openCharStack.pop()
                if openCharStack:
                    expectedClosingChar = CHARSDICT[openCharStack[-1]]
        if illegalCharsListLine:
            illegalCharsList.append(illegalCharsListLine[0])
        else:
            for i in range(len(openCharStack) -1, -1, -1):
                char = openCharStack[i]
                closingCharsListLine.append(CHARSDICT[char])
            closingCharsList.append(closingCharsListLine)
    return illegalCharsList, closingCharsList[::-1]

def getSyntaxScore(illegalCharsList):
    syntaxScore = 0
    for char in illegalCharsList:
        syntaxScore += CHARSSCOREDICT[char]
    return syntaxScore

def getAutoCompleteScore(closingCharsList):
    autoCompleteScore = 0
    autoCompleteScoreList = []
    for charList in closingCharsList:
        lineScore = 0
        for char in charList:
            lineScore = lineScore * 5
            lineScore += (CHARSSCOREDICTPART2[char])
        autoCompleteScoreList.append(lineScore)
    autoCompleteScoreList.sort()
    return autoCompleteScoreList[len(autoCompleteScoreList)//2]

illegalCharsList, closingCharsList = getIllegalCharacters(inputfile)
print(illegalCharsList)
syntaxScore = getSyntaxScore(illegalCharsList)
print(syntaxScore)
print()
print(closingCharsList)
print(getAutoCompleteScore(closingCharsList))