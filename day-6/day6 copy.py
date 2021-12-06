inputfile = open('day-6/day6_input.txt', 'r')
# inputfile = open('day-6/day6_input_ex.txt', 'r')

input = [int(val) for val in inputfile.read().split(',')]

# Make a list with a number for every day in the cycle
days = [0] * 9

for fish in input:
    print(fish)

    days[fish] += 1 
    print(days)

for i in range(256):
    today = i % len(days) # To make it cyclic: 0, 1, 2, 3, 4, 5, 6, 7, 8
    # Add new babies
    days[(today + 7) % len(days)] += days[today]
    
print(f'Total lanternfish after 256 days: {sum(days)}')