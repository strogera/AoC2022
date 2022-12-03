with open("input.txt", "r") as inputFile:
    lines = inputFile.read().splitlines()

    getPriorities = lambda l: sum(ord(c) - (ord('a') - 1 if c.islower() else ord('A') - 27) for c in l)
    intersect = lambda a, b, c = "": set(a).intersection(set(b)).intersection(set(c if c != "" else b)).pop()

    print(getPriorities([intersect(line[:len(line) // 2], line[len(line) // 2:]) for line in lines]))
    print(getPriorities([intersect(*lines[ptr: ptr + 3]) for ptr in range(0, len(lines), 3)]))