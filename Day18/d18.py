distance = lambda a, b: abs(a - b)


def getAdj(x, y, z):
    yield (x, y, z + 1)
    yield (x, y, z - 1)
    yield (x, y + 1, z)
    yield (x, y - 1, z)
    yield (x + 1, y, z)
    yield (x - 1, y, z)


def getSurface(cubes):
    count = len(cubes) * 6
    for (x, y, z) in cubes:
        for adj in getAdj(x, y, z):
            if adj in cubes:
                count -= 1
    return count


with open("input.txt", "r") as inputFile:
    cubes = [
        tuple(map(int, line.split(',')))
        for line in inputFile.read().splitlines()
    ]

    maxx = max([x for x, _, _ in cubes]) + 1
    maxy = max([y for _, y, z in cubes]) + 1
    maxz = max([z for _, _, z in cubes]) + 1
    minx, miny, minz = 0, 0, 0

    part1 = getSurface(cubes)
    print(part1)

    q = [(minx, miny, minz)]
    visited = set(cubes)
    while q:
        v = q.pop()
        visited.add(v)
        for adjx, adjy, adjz in getAdj(*v):
            if (adjx, adjy, adjz) in visited or adjx not in range(
                    minx, maxx) or adjy not in range(
                        miny, maxy) or adjz not in range(minz, maxz):
                continue
            q.append((adjx, adjy, adjz))

    cubes2 = set()
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            for z in range(minz, maxz):
                if (x, y, z) not in visited:
                    cubes2.add((x, y, z))
    print(part1 - getSurface(cubes2))