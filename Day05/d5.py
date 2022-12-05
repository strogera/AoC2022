with open("input.txt", "r") as inputFile:
    stacks = [[] for _ in range(10)]
    inputStacks, inputCmds = inputFile.read().split("\n\n")
    for x in inputStacks.split('\n')[:-1]:
        l = x.replace('[', ' ').replace(']', ' ')
        for i in range(1, len(l), 4):
            if(l[i] != ' '):
                stacks[i//4 + 1].append(l[i])
    stacks2 = [x.copy() for x in stacks]
    for x in (y.replace('move ', '').replace('from ', '').replace('to ', '') for y in inputCmds.split('\n')):
        n, src , dest = map(int, x.split(' '))
        items = [stacks[src].pop(0) for _ in range(n)]
        items2 = [stacks2[src].pop(0) for _ in range(n)]
        stacks[dest] =  items[::-1] + stacks[dest]
        stacks2[dest] =  items2 + stacks2[dest]
    getAns = lambda x: ''.join([x[0] for x in filter(lambda k: len(k) > 0, x)])
    print(getAns(stacks))
    print(getAns(stacks2))
