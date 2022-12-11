from math import prod, lcm
from functools import reduce
from copy import deepcopy


class Monkey:

    def __init__(self, monkeyStr):
        itemsStr, operationStr, testStr, iftrueStr, iffalseStr = monkeyStr.split('\n')[1:]
        self.items = list(map(int, itemsStr.split(':')[1].split(',')))
        op, operant = operationStr.split(' ')[-2:]
        getOperant = lambda a: int(operant) if operant != 'old' else a
        self.operation = lambda a: (a + getOperant(a) if op == '+' else a * getOperant(a))
        self.test = lambda a: int(iftrueStr.split(' ')[-1]) if (a % int(testStr.split(' ')[-1]) == 0) else int(iffalseStr.split(' ')[-1])
        self.countInspectedItems = 0

    def inspectItems(self, monkeys, reduceValue=0):
        for i in range(len(self.items)):
            curItem = self.operation(self.items[i])
            if reduceValue != 0:
                curItem %= reduceValue
            else:
                curItem //= 3
            monkeys[self.test(curItem)].items.append(curItem)
        self.countInspectedItems += len(self.items)
        self.items = []


with open("input.txt", "r") as inputFile:
    monkeysOriginal = []
    for m in inputFile.read().split('\n\n'):
        monkeysOriginal.append(Monkey(m))

    monkeys = deepcopy(monkeysOriginal)
    for _ in range(20):
        for m in monkeys:
            m.inspectItems(monkeys)

    reduceValue = lcm(*reduce(lambda a, b: a + b, (x.items for x in monkeysOriginal)))
    for _ in range(10000):
        for m in monkeysOriginal:
            m.inspectItems(monkeysOriginal, reduceValue)

    getAns = lambda monkeys: prod(sorted([x.countInspectedItems for x in monkeys], reverse=True)[:2])
    print(getAns(monkeys))
    print(getAns(monkeysOriginal))
