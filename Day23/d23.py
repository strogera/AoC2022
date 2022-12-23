from collections import defaultdict


def allEmptyAdj(elf, elves):
    for i in [-1, 0, 1]:
        for j in [-1j, 0, 1j]:
            if i == 0 and j == 0:
                continue
            if elf + i + j in elves:
                return False
    return True


def getPart1Ans(elves):
    maxx = int(max(el.real for el in elves.keys()))
    maxy = int(max(el.imag for el in elves.keys()))
    minx = int(min(el.real for el in elves.keys()))
    miny = int(min(el.imag for el in elves.keys()))
    count = 0
    for i in range(minx, maxx + 1):
        for j in range(miny, maxy + 1):
            if complex(i, j) not in elves:
                count += 1
    return count


with open("input.txt", "r") as inputFile:
    elves = {}
    for i, line in enumerate(inputFile.read().splitlines()):
        for j, c in enumerate(line):
            if c == '#':
                elves[complex(i, j)] = True

    direction = [-1, 1, -1j, 1j]
    moved = True
    round = 0
    while moved:
        moved = False
        if round == 10:
            print(getPart1Ans(elves))
        round += 1
        proposedMoves = {}
        freq = defaultdict(int)
        for elf in elves:
            if allEmptyAdj(elf, elves):
                continue
            for d in direction:
                if all(elf + d + inc not in elves for inc in (
                    [-1j, 0, 1j] if d.imag == 0 else [-1, 0, 1])):
                    proposedMoves[elf + d] = elf
                    freq[elf + d] += 1
                    freq[elf] += 1
                    break
        for movePos in proposedMoves:
            if freq[movePos] == 1:
                moved = True
                elves.pop(proposedMoves[movePos])
                elves[movePos] = True
        direction = direction[1:] + [direction[0]]
    print(round)