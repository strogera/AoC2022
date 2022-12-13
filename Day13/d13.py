from enum import Enum
from ast import literal_eval


class Result(Enum):
    EQ = 0,
    ORDER = 1,
    NOTORDER = 2


class Packet:

    def __init__(self, l):
        self.l = l

    def __eq__(self, __o: object) -> bool:
        return comparePackets(self.l, __o.l) == Result.EQ

    def __lt__(self, __o: object) -> bool:
        return comparePackets(self.l, __o.l) == Result.ORDER


def comparePackets(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 == p2:
            return Result.EQ
        return Result.ORDER if p1 < p2 else Result.NOTORDER
    if isinstance(p1, int):
        return comparePackets([p1], p2)
    elif isinstance(p2, int):
        return comparePackets(p1, [p2])
    i = 0
    while i < len(p1) and i < len(p2):
        if (cur := comparePackets(p1[i], p2[i])) != Result.EQ:
            return cur
        i += 1
    if len(p1) < len(p2):
        return Result.ORDER
    return Result.EQ if len(p1) == len(p2) else Result.NOTORDER


with open("input.txt", "r") as inputFile:
    packets = [literal_eval(x) for p in inputFile.read().split("\n\n") for x in p.split('\n')]
    ans1 = 0
    for i in range(0, len(packets) - 1, 2):
        if comparePackets(packets[i], packets[i + 1]) != Result.NOTORDER:
            ans1 += i // 2 + 1
    print(ans1)
    packets.append([[2]])
    packets.append([[6]])
    ls = [x.l for x in sorted([Packet(p) for p in packets])]
    print((ls.index([[2]]) + 1) * (ls.index([[6]]) + 1))