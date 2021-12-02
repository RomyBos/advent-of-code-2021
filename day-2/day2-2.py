inputfile = open('day-2/day2_input.txt', 'r')
Lines = inputfile.readlines()

horizontal_position = 0
depth_position = 0
aim = 0

for line in Lines:
    line = line.strip().split()
    instruction = line[0]
    units = int(line[1])
    if instruction == 'forward':
        horizontal_position += units
        depth_position += (units * aim)
    elif instruction == 'up':
        aim -= units
    elif instruction == 'down':
        aim += units
    else:
        print('unknown instruction')
        break
print("Final horizontal position: " + str(horizontal_position))
print("Final depth: " + str(depth_position))
print("Horizontal and depth multiplied: " + str(horizontal_position*depth_position))
    