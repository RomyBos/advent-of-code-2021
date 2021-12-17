import numpy as np

inputfile = open('day-13/day13_input.txt', 'r')
#inputfile = open('day-13/day13_input_ex.txt', 'r')

def placeDotsOnMatrix(M, dots):
    pass

def getDotsAndFolds(inputfile):
    pass

def getMatrix(inputfile):
    listOfCoords = []
    listFoldLines = []
    n = 0
    m = 0
    # Get a matrix of dots
    with inputfile as f:
        for line in f.readlines():
            if line == '\n':
                continue
            if line.startswith("fold along"):
                foldLine = line.replace('fold along ', '')
                coord, value = foldLine.strip().split("=")
                listFoldLines.append({'coord': coord, 'value': int(value)})
                continue
            x, y = map(int, line.strip().split(","))
            listOfCoords.append((x, y))
            if x > n:
                n = x
            if y > m:
                m = y
    
    array = [ [ "." for i in range(n+1) ] for j in range(m+1) ]
    M = np.array(array)

    # Fill matrix with #'s
    for coord in listOfCoords:
        M = M.transpose()
        M[(coord)] = '#'
        M = M.transpose()
            
    return M, listFoldLines

def foldLines(M, listFoldLines):
    for fold in listFoldLines:
        coord = fold['coord']
        value = fold['value']
        if coord == 'x':
            M = M.transpose()
        #M = np.delete(M, value, axis=0) # Delete fold line
        newArray = []
        matchingRow = 2
        # array = [ [ "." for i in range(n+1) ] for j in range(m+1) ]
        for i in range(len(M)):
            # if i < value:
            #     newArray.append(M[i])
            if i > value:
                newRow = getMergedRow(M[i-matchingRow], M[i])
                newArray.append(newRow)
                matchingRow += 2
        M = np.array(newArray)
        M = np.flipud(M)
        if coord == 'x':
            M = M.transpose()
    return M

def getMergedRow(row1, row2):
    mergedRow = []
    for i in range(len(row1)):
        if row1[i] == '#' or row2[i] == '#':
            mergedRow.append('#')
        else:
            mergedRow.append('.')
    return mergedRow

M, listFoldLines = getMatrix(inputfile)
print(M, '\n', listFoldLines)

M = foldLines(M, listFoldLines)
print(M)

countDots = 0
for row in M:
    for pt in row:
        if pt == '#':
            countDots += 1

print(countDots)