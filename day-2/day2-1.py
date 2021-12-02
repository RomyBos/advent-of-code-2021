inputfile = open('day-2/day2_input.txt', 'r')
Lines = inputfile.readlines()

def get_horizontal_and_depth(Lines):
    horizontal = 0
    depth = 0
    for line in Lines:
        line = line.strip().split()
        if line[0] == 'forward':
            horizontal += int(line[1])
        elif line[0] == 'up':
            depth -= int(line[1])
        elif line[0] == 'down':
            depth += int(line[1])
        else:
            print('unknown instruction')
            break
    return(horizontal, depth)

def get_horizontal_depth_multiplied(horizontal, depth):
    return horizontal * depth

horizontal, depth = get_horizontal_and_depth(Lines)

print("Final horizontal position: " + str(horizontal))
print("Final depth: " + str(depth))
print("Horizontal and depth multiplied: " + str(get_horizontal_depth_multiplied(horizontal, depth)))
    