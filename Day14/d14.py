from collections import defaultdict

air = 0
wall = 1
sand = 2


def moveDown(grid, cur, lowestWall, part2=False):
    next = cur[0], cur[1] + 1
    if part2:
        if next[1] == lowestWall:
            grid[next] = wall
            grid[next[0] + 1, next[1]] = wall
            grid[next[0] - 1, next[1]] = wall
    if grid[next] == air:
        if cur[1] > lowestWall:
            return False
    else:
        next = cur[0] - 1, cur[1] + 1
        if grid[next] != air:
            next = cur[0] + 1, cur[1] + 1
            if grid[next] != air:
                grid[cur] = sand
                return cur
    return moveDown(grid, next, lowestWall, part2)


with open("input.txt", "r") as inputFile:
    origGrid = defaultdict(int)
    source = (500, 0)
    walls = inputFile.read().splitlines()
    for w in walls:
        ws = w.split(' -> ')
        prev = None
        for cur in ws:
            x, y = map(int, cur.split(','))
            if prev != None:
                r = range(prev[1], y + 1) if prev[1] < y else range(prev[1], y - 1, -1)
                for yi in r:
                    origGrid[x, yi] = wall
                r = range(prev[0], x + 1) if prev[0] < x else range(prev[0], x - 1, -1)
                for xi in r:
                    origGrid[xi, y] = wall
            prev = (x, y)

    lowestWall = max([k[1] for k in origGrid.keys()])
    grid = origGrid.copy()
    while moveDown(grid, source, lowestWall):
        pass

    print(list(grid.values()).count(sand))

    grid = origGrid.copy()
    while moveDown(grid, source, lowestWall + 2, part2=True) != source:
        pass
    print(list(grid.values()).count(sand))