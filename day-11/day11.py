import numpy as np
inputfile = open('day-11/day11_input.txt', 'r')
# inputfile = open('day-11/day11_input_ex.txt', 'r')

def getMatrix(inputfile):
    array = []
    with inputfile as f:
        for line in f.readlines():
            row = list(map(int, line.strip()))
            array.append(row)
    return np.array(array)

def nextStep(M, amountOfFlashes):
    M = M.copy()
    listOfFlashed = []
    # First, the energy level of each octopus increases by 1.
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i, j] += 1
    # Then, any octopus with an energy level greater than 9 flashes.
    for i in range(len(M)):
        for j in range(len(M[i])):
            energyLevel = M[i, j]
            if energyLevel > 9 and (i, j) not in listOfFlashed:
                M, listOfFlashed = flash(M, (i, j), listOfFlashed)
    # Finally, any octopus that flashed during this step has its energy level set to 0
    for pos in listOfFlashed:
        amountOfFlashes += 1 # TODO: move out of here
        M[pos] = 0
    return M, amountOfFlashes, len(listOfFlashed)

def flash(M, pos, listOfFlashed):
    neighbours = getNeighbours(M, pos)
    listOfFlashed.append(pos) # flash
    for neighbour in neighbours:
        M[neighbour] += 1
    for neighbour in neighbours:
        energyLevel = M[neighbour]
        if energyLevel > 9 and neighbour not in listOfFlashed:
            M, listOfFlashed = flash(M, neighbour, listOfFlashed)
    return M, listOfFlashed


def getNeighbours(M, pos):
    neighbours = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, M.shape[0])
            rangeY = range(0, M.shape[1])
            (newX, newY) = (pos[0]+dx, pos[1]+dy)
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                neighbours.append((newX, newY))
    return neighbours

M = getMatrix(inputfile)
print(M)
amountOfFlashes = 0

for i in range(1000):
    M, amountOfFlashes, listOfFlashed = nextStep(M, amountOfFlashes)
    if listOfFlashed == M.size:
        print(i+1)

print("Result:")

print(amountOfFlashes)
