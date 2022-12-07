from collections import defaultdict

with open("input.txt", "r") as inputFile:
    curPath = []
    filePaths = defaultdict(int)

    for line in inputFile.read().splitlines():
        if line[0] == '$':
            cmd = line[2:].split(' ')
            if cmd[0] == 'cd':
                if cmd[1] != '..':
                    curPath.append(cmd[1])
                else:
                    curPath.pop()
        else:
            output = line.split(' ')
            if output[0] != 'dir':
                for i in range(len(curPath)):
                    filePaths['+'.join(curPath[:i + 1])] += int(output[0])

    fileSizes = sorted(filePaths.values())
    i = 0
    ans1 = 0
    while fileSizes[i] <= 100000:
        ans1 += fileSizes[i]
        i += 1
    print(ans1)

    required = 30_000_000 - (70_000_000 - filePaths['/'])
    i = 0
    while fileSizes[i] < required:
        i += 1
    print(fileSizes[i])
