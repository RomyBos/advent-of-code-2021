inputfile = open('day-10/day10_input.txt', 'r')
# inputfile = open('day-10/day10_input_ex.txt', 'r')

OPENING_CHARS = ['(', '[', '{', '<']
CLOSING_CHARS = [')', ']', '}', '>']
CHARSDICT = {'(': ')', '[': ']', '{': '}', '<': '>'}
CHARSSCOREDICT = {')': 3, ']': 57, '}': 1197, '>': 25137}

def getIllegalCharacters(inputfile):
    illegalCharsList = []
    lines = inputfile.readlines()
    for i in range(len(lines)):
        openCharStack = []
        illegalCharsListLine = []
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
    return illegalCharsList

def getSyntaxScore(illegalCharsList):
    syntaxScore = 0
    for char in illegalCharsList:
        syntaxScore += CHARSSCOREDICT[char]
    return syntaxScore

illegalCharsList = getIllegalCharacters(inputfile)
print(illegalCharsList)
syntaxScore = getSyntaxScore(illegalCharsList)
print(syntaxScore)