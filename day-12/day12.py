inputfile = open('day-12/day12_input.txt', 'r')
# inputfile = open('day-12/day12_input_ex.txt', 'r')


def getHallways(inputfile):
    lines = inputfile.readlines()
    dictOfHallways = {}
    for line in lines:
        listOfWays = []
        start, end = line.strip().split('-')
        try:
            listOfWays = dictOfHallways[start]
        except KeyError:
            pass
        listOfWays.append(end)
        dictOfHallways[start] = (listOfWays)

        listOfWays = []
        try:
            listOfWays = dictOfHallways[end]
        except KeyError:
            pass
        listOfWays.append(start)
        dictOfHallways[end] = (listOfWays)

    return dictOfHallways

def getAllPossiblePaths(dictOfHallways, allPossiblePaths, path, startCaveExit):
    path = path.copy()
    allPossiblePaths = allPossiblePaths.copy()
    path.append(startCaveExit)
    startCaveExits = getCaveExits(dictOfHallways, startCaveExit)
    for exit in startCaveExits:
        count = path.count(exit)
        smallCaveVisitedTwice = isSmallCaveVisitedTwice(path)
        if exit == 'start':
            continue
        elif exit.islower() and smallCaveVisitedTwice and exit in path:
            continue
        elif exit.islower() and path.count(exit) > 1 and not smallCaveVisitedTwice:
            continue
        elif exit == 'end':
            endpath = path.copy()
            endpath.append(exit)
            allPossiblePaths.append(endpath)
        else:
            allPossiblePaths = getAllPossiblePaths(dictOfHallways, allPossiblePaths, path, exit)

    return allPossiblePaths

def isSmallCaveVisitedTwice(path):
    for x in path:
        if x.islower():
            if path.count(x) > 1:
                return True
    return False

def getCaveExits(dictOfHallways, cave):
    caveExits = dictOfHallways[cave]
    return caveExits


print()
dictOfHallways = getHallways(inputfile)
print(dictOfHallways)

startExit = 'start'

allPossiblePaths = getAllPossiblePaths(dictOfHallways, [], [], startExit)

print("Result:")
for path in allPossiblePaths:
    print(path)

print("amount of paths:")
print(len(allPossiblePaths))