import heapq


def isInRange(grid, x, y):
    return x in range(len(grid)) and y in range(len(grid[x]))


def getAdj(grid, x, y):
    for i in [-1, 1]:
        if isInRange(grid, x + i,
                     y) and (ord(grid[x + i][y]) - ord(grid[x][y]) <= 1
                             or grid[x][y] == 'S' or
                             (grid[x][y] == 'z' and grid[x + i][y] == 'E')):
            yield (x + i, y)
        if isInRange(grid, x, y +
                     i) and (ord(grid[x][y + i]) - ord(grid[x][y]) <= 1
                             or grid[x][y] == 'S' or
                             (grid[x][y] == 'z' and grid[x][y + i] == 'E')):
            yield (x, y + i)


cache = {}
def findPath(grid, start, end, part2=False):
    dist = {}
    queue = [(0, start)]
    heapq.heapify(queue)
    dist[start] = 0
    prev = {}
    visited = set()
    while queue:
        d, v = heapq.heappop(queue)
        if v == end:
            cur = end
            i = 1
            while cur != start:
                cache[cur] = i
                cur = prev[cur]
                i += 1
            return d
        if v in visited:
            continue
        visited.add(v)
        for x, y in getAdj(grid, v[0], v[1]):
            alt = d + 1
            if (x, y) not in dist or alt < dist[(x, y)]:
                prev[(x, y)] = v
                if (x, y) in cache:
                    return d + cache[(x, y)]
                dist[(x, y)] = alt
                heapq.heappush(queue, (alt, (x, y)))


with open("input.txt", "r") as inputFile:
    grid = inputFile.read().splitlines()
    start, end = (0, 0), (0, 0)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'S':
                start = (x, y)
            elif grid[x][y] == 'E':
                end = (x, y)
    print(findPath(grid, start, end))
    ans = 99999999
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'a':
                p = findPath(grid, (x, y), end)
                ans = min(ans, p if p != None else ans)
    print(ans)