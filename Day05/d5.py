with open("input.txt", "r") as inputFile:
    stacks = [[] for _ in range(10)]
    inputStacks, inputCmds = inputFile.read().split("\n\n")
    for line in inputStacks.split('\n')[:-1]:
        for i in range(1, len(line), 4):
            if(line[i] != ' '):
                stacks[i//4 + 1].append(line[i])
    stacks2 = [x.copy() for x in stacks]
    for x in (y.replace('move ', '').replace('from ', '').replace('to ', '') for y in inputCmds.split('\n')):
        n, src , dest = map(int, x.split(' '))
        stacks[dest] = stacks[src][:n][::-1] + stacks[dest]
        stacks2[dest] = stacks2[src][:n] + stacks2[dest]
        stacks[src] = stacks[src][n:]
        stacks2[src] = stacks2[src][n:]
    getAns = lambda x: ''.join([x[0] for x in filter(lambda k: len(k) > 0, x)])
    print(getAns(stacks))
    print(getAns(stacks2))