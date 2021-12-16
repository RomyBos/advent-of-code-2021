import numpy as np

# inputfile = open('day-13/day13_input.txt', 'r')
inputfile = open('day-13/day13_input_ex.txt', 'r')

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
            M.transpose()
        for i in range(len(M[value])):
            M[value, i] = '-'
        M = np.delete(M, value, axis=0)
        for i in M:
            
            print(i)


        break

M, listFoldLines = getMatrix(inputfile)
print(M, '\n', listFoldLines)

M = foldLines(M, listFoldLines)
