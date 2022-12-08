from collections import defaultdict

with open("input.txt", "r") as inputFile:
    grid = [[int(c) for c in line] for line in inputFile.read().splitlines()]
    counted = set()
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):
            if all(grid[i][y] < grid[x][y] for i in range(x)) or all(
                    grid[i][y] < grid[x][y]
                    for i in range(len(grid[x]) - 1, x, -1)) or all(
                        grid[x][i] < grid[x][y] for i in range(y)) or all(
                            grid[x][i] < grid[x][y]
                            for i in range(len(grid) - 1, y, -1)):
                counted.add((x, y))

    maxScore = 0
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):
            score = 1
            i = x - 1
            while i > 0 and grid[i][y] < grid[x][y]:
                i -= 1
            score *= x - i
            i = x + 1
            while i < len(grid) - 1 and grid[i][y] < grid[x][y]:
                i += 1
            score *= i - x
            i = y - 1
            while i > 0 and grid[x][i] < grid[x][y]:
                i -= 1
            score *= y - i
            i = y + 1
            while i < len(grid[x]) - 1 and grid[x][i] < grid[x][y]:
                i += 1
            score *= i - y
            maxScore = max(maxScore, score)

    print(len(counted) + 2 * (len(grid)) + 2 * (len(grid[0])) - 4)
    print(maxScore)
