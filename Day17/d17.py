from collections import defaultdict

def findCycle(grid):
    height = getHeight()
    getline = lambda x: [grid[i + x * 1j] for i in range(7)]
    cur = []
    for i in range(height, height // 2 - 1, -1):
        curLine = getline(i)
        cur.append(curLine)
        if len(cur) > 4 and all(getline(i - j - 1) == cur[j] for j in range(len(cur))):
            return len(cur)
    return 0


def collision(rock, grid):
    return any(grid[x] != 0 for x in rock)


def isInside(rock):
    return all(0 <= int(x.real) < 7 for x in rock)


with open("input.txt", "r") as inputFile:
    commands = inputFile.read()
    grid = defaultdict(int)
    for i in range(7):
        grid[i - 1j] = 1
    rocks = [[0, 1, 2, 3], [1j, 1, 1 + 1j, 1 + 2j, 2 + 1j],
             [0, 1, 2, 2 + 1j, 2 + 2j], [0, 1j, 2j, 3j], [0, 1j, 1, 1 + 1j]]

    maxHeight = -1

    def getHeight():
        global maxHeight
        return maxHeight

    def moveRock(source, curRock, step):
        rockPos = []
        for pos in curRock:
            rockPos.append(pos + source)
        while True:
            cmd = commands[step % len(commands)]
            step += 1
            for i in range(len(rockPos)):
                rockPos[i] += (1 if cmd == '>' else -1)
            if (not isInside(rockPos)) or collision(rockPos, grid):
                for i in range(len(rockPos)):
                    rockPos[i] -= (1 if cmd == '>' else -1)
            for i in range(len(rockPos)):
                rockPos[i] += -1j
            if collision(rockPos, grid):
                global maxHeight
                curHeight = maxHeight
                for pos in rockPos:
                    grid[pos + 1j] = 1
                    curHeight = max(curHeight, int((pos + 1j).imag))
                maxHeight = curHeight
                return step

    step = 0
    for countRocks in range(2022):
        curRock = rocks[countRocks % len(rocks)]
        source = 2 + (getHeight() + 4) * 1j
        step = moveRock(source, curRock, step)
    print(getHeight() + 1)

    grid.clear()
    for i in range(7):
        grid[i - 1j] = 1

    step = 0
    maxHeight = -1
    maxIter = 1000000000000
    rockCount = defaultdict(int)
    heightOfRock = defaultdict(int)
    for countRocks in range(maxIter):
        curRock = rocks[countRocks % len(rocks)]
        h = getHeight()
        source = 2 + (getHeight() + 4) * 1j
        step = moveRock(source, curRock, step)
        rockCount[getHeight()] = countRocks + 1
        heightOfRock[countRocks] = getHeight() - h

        if countRocks > 3000 and (c := findCycle(grid)) != 0:
            rocksInCycle = rockCount[getHeight()] - (
                rockCount[getHeight() - c])
            repeatingRocks = (maxIter - countRocks)
            reminderRocks = repeatingRocks % rocksInCycle
            ans = getHeight() + (repeatingRocks // rocksInCycle) * (c)
            for i in range(reminderRocks):
                ans += heightOfRock[countRocks - rocksInCycle + i]
            print(ans - 1)
            break
