import heapq

with open("input.txt", "r") as inputFile:
    startingPos = None
    targetPos = None
    inp = inputFile.read().splitlines()
    for i in range(len(inp[0])):
        if inp[0][i] == '.':
            startingPos = (i, 0)
            break
    for i in range(len(inp[0])):
        if inp[len(inp) - 1][i] == '.':
            targetPos = (i, len(inp) - 1)
            break

    maxy = len(inp)
    maxx = len(inp[0])

    def search(lines, start, end, time=0):
        # search from https://github.com/ephemient/aoc2022/blob/main/py/aoc2022/day24.py
        seen, queue = {(start, time)}, [(0, (start, time))]
        while queue:
            position, time = heapq.heappop(queue)[1]
            if position == end:
                return time
            x, y = position
            time += 1
            for x, y in [(x - 1, y), (x, y - 1), (x, y), (x, y + 1),
                         (x + 1, y)]:
                if y < 0 or y >= maxy or x < 1 or x >= maxx - 1:
                    continue
                line = lines[y]
                if y in (0, maxy - 1):
                    if line[x] != ".":
                        continue
                elif lines[y][(x - 1 + time) % (maxx - 2) + 1] == "<":
                    continue
                elif lines[y][(x - 1 - time) % (maxx - 2) + 1] == ">":
                    continue
                elif lines[(y - 1 + time) % (maxy - 2) + 1][x] == "^":
                    continue
                elif lines[(y - 1 - time) % (maxy - 2) + 1][x] == "v":
                    continue
                state = ((x, y), time)
                if state not in seen:
                    seen.add(state)
                    heapq.heappush(
                        queue, (time + abs(x - end[1]) + abs(y - end[0]), state))

    first = search(inp, startingPos, targetPos)
    print(first)
    second = search(inp, targetPos, startingPos, first)
    print(search(inp, startingPos, targetPos, second))
