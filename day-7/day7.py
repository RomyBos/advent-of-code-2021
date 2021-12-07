import numpy as np

inputfile = open('day-7/day7_input.txt', 'r')
# inputfile = open('day-7/day7_input_ex.txt', 'r')

input = [int(val) for val in inputfile.read().split(',')]

def getFuelSpentForPosition(crabPositions):
    fuelSpentList = []
    for i in range(len(crabPositions)):
        fuelSpent = 0
        for crab in crabPositions:
            distanceToPosition = getFuelSpent(crab, i)
            fuelSpent += distanceToPosition
        
        fuelSpentList.append(fuelSpent)

    return fuelSpentList

def getFuelSpent(crab, position):
    distance = abs(crab - position)
    # Part 2
    fuelSpent = 0
    stepPrice = 0
    for i in range(distance):   # This should be replaced by a function that does this in one go
        stepPrice = stepPrice + 1
        fuelSpent += stepPrice

    return fuelSpent

def getBestPosition(fuelSpentList):
    return min(fuelSpentList)

fuelSpentList = getFuelSpentForPosition(input)
print (fuelSpentList)

print(getBestPosition(fuelSpentList))