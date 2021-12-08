inputfile = open('day-8/day8_input.txt', 'r')

def getDigitsList(inputfile):
    digitsList = []
    with inputfile as f:
        for line in f.readlines():
            lineEntry = []
            line = line.strip()
            pattern, output = line.split(' | ')
            pattern = pattern.split()
            output = output.split()
            lineEntry.append({'pattern': pattern, 'output': output})
            digitsList.append(lineEntry)
    return digitsList

def getEasyDigits(digitsList):
    results = [0] * 10
    for entry in digitsList:
        output = entry[0]["output"]
        for digit in output:
            digitlength = len(digit)
            if digitlength == 2:
                results[0] += 1
            elif digitlength == 4:
                results[4] += 1
            elif digitlength == 3:
                results[7] += 1
            elif digitlength == 7:
                results[8] += 1
    print(sum(results))

digitsList = getDigitsList(inputfile)
print(digitsList)

print(getEasyDigits(digitsList))