memo ={}
def simulate(minute, costs, ore= 0, clay= 0, obs= 0, oreBots= 1, clayBots = 0, obsBots = 0):
    if minute <= 1:
        return 0
    oreCost = costs[0]
    clayOreCost = costs[1]
    obsidianCostOre = costs[2][0]
    obsidianCostClay = costs[2][1]
    geodeCostOre = costs[3][0]
    geodeCostObsidian =costs[3][1]
    state = (minute, oreCost, clayOreCost, obsidianCostOre, obsidianCostClay, geodeCostOre, geodeCostObsidian, ore, clay, obs, oreBots, clayBots, obsBots)
    if state in memo:
        return memo[state]

    maxOreBots = (max(clayOreCost, obsidianCostOre, geodeCostOre, oreCost) * minute - ore) // minute + 1
    maxClayBots = (obsidianCostClay * minute - clay) // minute + 1
    maxObsBots =   (geodeCostObsidian * minute - obs) // minute + 1
    needOre = oreBots < maxOreBots
    needClay = clayBots < maxClayBots
    needObs = obsBots < maxObsBots

    res = 0
    if ore >= geodeCostOre and obs >= geodeCostObsidian:
        oreN = ore + oreBots
        clayN = clay + clayBots
        obsN = obs + obsBots
        res = max(res, simulate(minute - 1, costs, oreN - geodeCostOre, clayN, obsN - geodeCostObsidian, oreBots, clayBots, obsBots) + minute - 1 )
    elif needObs and ore >=obsidianCostOre and clay >= obsidianCostClay:
        oreN = ore + oreBots
        clayN = clay + clayBots
        obsN = obs + obsBots
        res = max(res, simulate(minute - 1, costs, oreN - obsidianCostOre, clayN - obsidianCostClay, obsN , oreBots, clayBots, obsBots + 1))
    else:
        if needOre and ore >= oreCost:
            oreN = ore + oreBots
            clayN = clay + clayBots
            obsN = obs + obsBots
            res = max(res, simulate(minute - 1, costs, oreN - oreCost, clayN, obsN , oreBots + 1, clayBots, obsBots) )
        if needClay and ore >= clayOreCost and needObs:
            oreN = ore + oreBots
            clayN = clay + clayBots
            obsN = obs + obsBots
            res = max(res, simulate(minute - 1, costs, oreN - clayOreCost, clayN, obsN , oreBots , clayBots + 1, obsBots))
        if needOre or needClay:
            oreN = ore + oreBots
            clayN = clay + clayBots
            obsN = obs + obsBots
            res = max(res, simulate(minute - 1, costs, oreN, clayN, obsN , oreBots , clayBots, obsBots))
    memo[state] = res
    return res




with open("input.txt", "r") as inputFile:
    blueprints = []
    for line in inputFile.read().splitlines():
        l = line.split(' ')
        id = int(l[1][:-1])
        oreCost = int(l[6])
        clayCost = int(l[12])
        obsidianCost = (int(l[18]), int(l[21]))
        geodeCost = (int(l[27]), int(l[30]))
        blueprints.append( [oreCost, clayCost, obsidianCost, geodeCost])

    ans1 = 0
    for i, b in enumerate(blueprints):
        ans1 += (i + 1) * simulate(24, b)
    print(ans1)
    ans2 = 1
    for i in range(3):
        ans2 *= simulate(32, blueprints[i])
    print(ans2)
