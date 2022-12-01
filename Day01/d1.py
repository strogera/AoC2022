with open("input.txt", "r") as inputFile:
    elves = sorted([sum([int(z) for z in x]) for x in [y.strip().split('\n') for y in inputFile.read().strip().split('\n\n')]])
    print(elves[-1])
    print(sum(elves[-3:]))