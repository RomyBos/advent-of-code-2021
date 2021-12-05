from pandas import *
import numpy as np

inputfile = open('day-5/day5_input.txt', 'r')
# inputfile = open('day-5/day5_input_ex.txt', 'r')

MATRIX_SIZE = 1000
# MATRIX_SIZE = 10

def getLineCoordinatesList(inputfile):
    lineCoordinatesList = []
    with inputfile as f:
        for line in f.readlines():
            lineCoordinates = []
            line = line.strip()
            start, end = line.split(' -> ')
            x1, y1 = start.split(',')
            x2, y2 = end.split(',')
            lineCoordinates.append((int(x1), int(y1)))
            lineCoordinates.append((int(x2), int(y2)))
            lineCoordinatesList.append(lineCoordinates)
    return lineCoordinatesList

def getNumOverlappingLines(matrix):
    matrix = np.transpose(matrix)

    countOverlappingLines = 0
    for row in matrix:
        for place in row:
            if place > 1:
                countOverlappingLines += 1
    # print(matrix)
    print(countOverlappingLines)

def drawLinesOnMatrix(matrix, lineCoordinatesList):
    matrix = matrix.copy()
    for lineCoordinates in lineCoordinatesList:
        start, end = lineCoordinates
        x1, y1 = start
        x2, y2 = end
        # Check if coordinates match (no line)
        if (x1, y1) == (x2, y2):
            matrix[x1, y1] += 1
        else:
            # Swap axes if Y slope is smaller than X slope
            transpose = np.absolute(x2 - x1) < np.absolute(y2 - y1) # The absolute value of a number is the number's distance from 0. This makes any negative number positive, while positive numbers are unaffected.
            if transpose:
                matrix = np.transpose(matrix)
                x1, y1, x2, y2 = y1, x1, y2, x2

            # Swap direction if necesarry
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1

            # Mark the start and the end
            matrix[x1, y1] += 1
            matrix[x2, y2] += 1

            # Calculate all points between start and end
            x = np.arange(x1 + 1, x2)
            y = np.round(((y2 - y1) / (x2 - x1)) * (x - x1) + y1).astype(x.dtype)
            matrix[x, y] += 1

            if transpose:
                matrix= matrix.T

    return matrix

def getMatrix(size):
    return np.zeros((size, size), dtype=int)

lineCoordinatesList = getLineCoordinatesList(inputfile)
matrix = getMatrix(MATRIX_SIZE)
matrix = drawLinesOnMatrix(matrix, lineCoordinatesList)

getNumOverlappingLines(matrix)