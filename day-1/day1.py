inputfile = open('day-1/day1_input.txt', 'r')
Lines = list(map(int, inputfile.readlines()))

def number_of_increases(Lines):
    number_of_increases = -1
    previous_line = 0
    for line in Lines:
        if previous_line < line:
            number_of_increases += 1
        previous_line = line
    return number_of_increases

def number_of_increases_slices(Lines):
    window_size = 3
    previous_line_slice = 0
    number_of_increases = -1
    for i in range(len(Lines) - window_size + 1):
        lineSum = sum(Lines[i: i + window_size])
        if previous_line_slice < lineSum:
            number_of_increases += 1
        previous_line_slice = lineSum
    return number_of_increases

print("1. Lines bigger than previous line: " + str(number_of_increases(Lines)))
print("2. Slice of Lines bigger than previous slice: " + str(number_of_increases_slices(Lines)))