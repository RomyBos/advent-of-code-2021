inputfile = open('day-2/day2_input.txt', 'r')
Lines = inputfile.readlines()

horizontal_position = 0
depth_position = 0

for line in Lines:
    line = line.strip().split()
    if line[0] == 'forward':
        horizontal_position += int(line[1])
    elif line[0] == 'up':
        depth_position -= int(line[1])
    elif line[0] == 'down':
        depth_position += int(line[1])
    else:
        print('unknown instruction')
        break
print("Final horizontal position: " + str(horizontal_position))
print("Final depth: " + str(depth_position))
print("Horizontal and depth multiplied: " + str(horizontal_position*depth_position))
    