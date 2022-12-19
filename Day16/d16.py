from copy import deepcopy
from collections import defaultdict

with open("input.txt", "r") as inputFile:
    valves = {}
    for line in inputFile.read().splitlines():
        l = line.split(' ')
        name = l[1]
        flow = int(l[4].split('=')[-1][:-1])
        connections = ''.join(l[9:]).split(',')
        valves[name] = (flow, connections)

    minDistance = {
        x: {y: 1 if y in valves[x][1] else 9999999
            for y in valves}
        for x in valves
    }

    # Floyd-Warshall
    for v1 in minDistance:
        for v2 in minDistance:
            for v3 in minDistance:
                minDistance[v2][v3] = min(minDistance[v2][v3], minDistance[v2][v1] + minDistance[v1][v3])

    memo = defaultdict(int)

    def openValve(name, state, minute, flow):
        hashableState = tuple(state.values())
        memo[hashableState] = max(memo[hashableState], flow)
        for v in filter(lambda a: not state[a], state):
            newMinute = minute - minDistance[name][v] - 1
            if newMinute <= 0:
                continue
            newState = deepcopy(state)
            newFlow = flow + valves[v][0] * newMinute
            newState[v] = True
            openValve(v, newState, newMinute, newFlow)

    state = {name: False for name in valves.keys() if valves[name][0] != 0}
    openValve('AA', state, 30, 0)
    print(max(memo.values()))

    state = {name: False for name in valves.keys() if valves[name][0] != 0}
    memo.clear()
    openValve('AA', state, 26, 0)
    ans = 0
    for s in memo:
        for s2 in memo:
            if all(not (s[i] and s2[i]) for i in range(len(s))):
                ans = max(ans, memo[s] + memo[s2])
    print(ans)