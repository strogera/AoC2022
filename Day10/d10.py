with open("input.txt", "r") as inputFile:
    x = 1
    xDuringCycle = [x]
    calcCycles = [20, 60, 100, 140, 180, 220]
    for line in inputFile.read().splitlines():
        op = line.split(' ')
        if op[0] == 'noop':
            xDuringCycle.append(x)
        else:
            xDuringCycle.append(x)
            xDuringCycle.append(x)
            x += int(op[1])
    print(sum([xDuringCycle[i] * i for i in calcCycles]))

    output = []
    for curPixel, sprite in enumerate(xDuringCycle[1:]):
        sPos = [sprite - 1, sprite, sprite + 1]
        if (curPixel % 40) in sPos:
            output.append('#')
        else:
            output.append(' ')

        curPixel += 1
    for i in range(0, len(output), 40):
        print(''.join(output[i:i + 40]))
