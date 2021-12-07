inputfile = open('day-6/day6_input.txt', 'r')
# inputfile = open('day-6/day6_input_ex.txt', 'r')

input = [int(val) for val in inputfile.read().split(',')]

# At first I did it with a bunch of for loops, goign through everything and adding to the list.
# Part 2, with 256 days, was in no way going to work like that. It took forever.
# In this solution we're remembering the amount of fish that are on each cycle day. We are taking advantage
# of the fact that this doesn't change.

def getCountLanternFishAfterDays(fishList, days):
    fishList = fishList.copy()
    countLanternFish = len(fishList)

    # Make a list with a number for every day in the cycle
    cycleList = [0] * 9

    # Count the amount of fish that are on each day of the cycle
    for fishAge in fishList:
        cycleList[fishAge] += 1 

    for i in range(days):
        # Cycle through cycle days 0 - 8 (Not my own idea)
        today = i % 9
        amountOfFishToday = cycleList[today]
        babyReadyDay = today + 7
        babyReadyCycleDay = babyReadyDay % 9
        cycleList[babyReadyCycleDay] += amountOfFishToday

        # Old Solution
        # for j in range(len(fishList)):
        #     fishAge = fishList[j]
        #     if fishAge == 0:
        #         fishList[j] = 6
        #         fishList.append(8)
        #     else:
        #         fishList[j] -= 1

    countLanternFish = sum(cycleList)

    return countLanternFish

print (getCountLanternFishAfterDays(input, 256))