from os import read
import numpy as np

#inputfile = open('day-9/day9_input.txt', 'r')
inputfile = open('day-9/day9_input_ex.txt', 'r')

def getMatrix(inputfile):
    array = []
    with inputfile as f:
        for line in f.readlines():
            row = list(map(int, line.strip()))
            array.append(row)
    return np.array(array)

def getNeighbours(M, i, j):
    neighbours = []
    if i > 0: # If there's anything on the top
        neighbours.append((i-1, j))
    if i+1 < len(M): # If there's anything on the bottom
        neighbours.append((i+1,j))
    if j > 0: # If anything on the left
        neighbours.append((i,j-1))
    if j+1 < len(M[i]): # if anything on the right
        neighbours.append((i,j+1))
    return neighbours

def getNeighbourValues(M, neighbours):
    neighbourValues = []
    for neighbour in neighbours:
        neighbourValues.append(M[neighbour])
    return neighbourValues

def getLowPoints(M):
    lowPointsList = []
    lowpointsCoords = []
    for i in range(len(M)):
        for j in range(len(M[i])):
            lowest = True
            point = M[i, j]
            neighbours = getNeighbours(M, i, j)
            neighbourValues = getNeighbourValues(M, neighbours)
            for neighbourValue in neighbourValues:
                if neighbourValue <= point:
                    lowest = False
            if lowest == True:
                lowPointsList.append(point)
                lowpointsCoords.append((i, j))
    return lowpointsCoords, lowPointsList

def getSumOfRiskLevels(lowPoints):
    sumOfRiskLevels = 0
    for point in lowPoints:
        sumOfRiskLevels += 1
        sumOfRiskLevels += point
    return sumOfRiskLevels

def getBasins(M, lowpointsCoords):
    basins = []
    for lowpoint in lowpointsCoords:
        x, y = lowpoint
        basinPoints = findNeighboursRecursively(M, x, y, [])
        print(basinPoints)
        basins.append(basinPoints)
        
    return basins

def findNeighboursRecursively(M, x, y, List):
    List = List.copy()
    List.append((x, y))

    neighbours = getNeighbours(M, x, y)
    for i in range(len(neighbours)-1, -1, -1):
        coord = neighbours[i]
        if coord in List:
            del neighbours[i]
        if M[coord] == 9:
            del neighbours[i]
    for point in neighbours:
        x2, y2 = point
        List = findNeighboursRecursively(M, x2, y2, List)
    print(getNeighbourValues(M, List))
    print(List)
    return List

def getSizeOfThreeiggestBasins(basins):
    result = 0
    basinSizes = []
    for i in range(len(basins)):
        basinSizes.append(len(basins[i]))
    result = np.prod(sorted(basinSizes, reverse=True)[:3])
    return result


M = getMatrix(inputfile)
print(M)
lowpointsCoords, lowPoints = getLowPoints(M)
print(lowPoints)
print(getSumOfRiskLevels(lowPoints))
print()
basins = getBasins(M, lowpointsCoords)
print(basins)
print(getSizeOfThreeiggestBasins(basins))