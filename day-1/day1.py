inputfile = open('day-1/day1_input.txt', 'r')
Lines = list(map(int, inputfile.readlines()))

window_size = 3
count = 0
previous_line = 0
previous_line_slice = 0
count_lines_larger_than_previous = -1
count_slice_of_lines_larger_than_previous = -1

for line in Lines:
    count += 1
    if previous_line < line:
        count_lines_larger_than_previous += 1
    previous_line = line

for i in range(len(Lines) - window_size + 1):
    lineSum = sum(Lines[i: i + window_size])
    # print(Lines[i: i + window_size])

    if previous_line_slice < lineSum:
        count_slice_of_lines_larger_than_previous += 1
    previous_line_slice = lineSum

print("Total count: " + str(count))
print("1. Lines bigger than previous line: " + str(count_lines_larger_than_previous))
print("2. Slice of Lines bigger than previous slice: " + str(count_slice_of_lines_larger_than_previous))