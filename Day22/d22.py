def parseCommands(commands):
    cmds = []
    i = 0
    while i < len(commands):
        c = commands[i]
        if c in 'RL':
            cmds.append(c)
            i += 1
        else:
            num = []
            while i < len(commands) and commands[i].isnumeric():
                num.append(commands[i])
                i += 1
            cmds.append(int(''.join(num)))
    return cmds


def findStartingPos():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                pos = complex(i, j)
                return pos


def wrapPart2(pos, dir):
    x, y = getCoordsFromComplex(pos)
    if dir.imag != 0:
        if x in range(1, 51):
            if y == 51:
                return complex(150 - x + 1, 1), 1j
            elif y == 150:
                return complex(150 - x + 1, 100), -1j
        elif x in range(51, 101):
            if y == 51:
                return complex(101, x - 50), 1
            elif y == 100:
                return complex(50, x + 50), -1
        elif x in range(101, 151):
            if y == 1:
                return complex(150 - x + 1, 51), 1j
            elif y == 100:
                return complex(150 - x + 1, 150), -1j
        elif x in range(151, 201):
            if y == 1:
                return complex(1, x - 100), 1
            elif y == 50:
                return complex(150, x - 100), -1
    else:
        if y in range(1, 51):
            if x == 101:
                return complex(50 + y, 51), 1j
            elif x == 200:
                return complex(1, y + 100), 1
        elif y in range(51, 101):
            if x == 1:
                return complex(y + 100, 1), 1j
            elif x == 150:
                return complex(y + 100, 50), -1j
        elif y in range(101, 151):
            if x == 1:
                return complex(200, y - 100), -1
            elif x == 50:
                return complex(y - 50, 100), -1j


with open("input.txt", "r") as inpuFile:
    gridInput, commands = inpuFile.read().split('\n\n')
    gridInput, commands = gridInput.splitlines(), commands.strip()
    maxLen = max((len(x) for x in gridInput))
    grid = [''.join(' ' for _ in range(maxLen + 2))]
    for line in gridInput:
        grid.append(' ' + line +
                    ''.join(' ' for _ in range((maxLen - len(line) + 1))))
    grid.append(''.join(' ' for _ in range(len(gridInput[0]) + 2)))

    cmds = parseCommands(commands)
    pos = findStartingPos()

    direction = 1j
    getCoordsFromComplex = lambda c: (int(c.real), int(c.imag))
    wrap2 = lambda a, b: complex(a % (len(grid)), b % (len(grid[0])))
    wrap = lambda a: wrap2(*getCoordsFromComplex(a))
    checkpoint = pos
    for cmd in cmds:
        if isinstance(cmd, int):
            i = 0
            while i <= cmd:
                pos = wrap(pos)
                x, y = getCoordsFromComplex(pos)
                if grid[x][y] == '.':
                    checkpoint = pos
                    pos += direction
                    i += 1
                elif grid[x][y] == '#':
                    break
                else:
                    pos += direction
            pos = checkpoint
        else:
            direction *= -1j if cmd == 'R' else 1j

    scoreDirection = [1j, 1, -1j, -1]
    x, y = getCoordsFromComplex(pos)
    print(1000 * x + 4 * y + scoreDirection.index(direction))

    pos = findStartingPos()
    direction = 1j
    p = 0
    for cmd in cmds:
        if isinstance(cmd, int):
            for i in range(cmd):
                curPos, curDirection = pos + direction, direction
                x, y = getCoordsFromComplex(curPos)
                if grid[x][y] == ' ':
                    curPos, curDirection = wrapPart2(pos, direction)
                    x, y = getCoordsFromComplex(curPos)
                if grid[x][y] == '#':
                    break
                pos, direction = curPos, curDirection
        else:
            direction *= -1j if cmd == 'R' else 1j

    x, y = getCoordsFromComplex(pos)
    print(1000 * x + 4 * y + scoreDirection.index(direction))
