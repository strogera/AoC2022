class Node:

    def __init__(self, n):
        self.n = n
        self.prev = self
        self.next = self

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def insertAfter(self, other):
        self.remove()
        self.prev = other
        self.next = other.next
        tmp = other.next
        other.next = self
        tmp.prev = self

    def move(self, i):
        if i == 0:
            return
        cur = self
        for _ in range(i):
            cur = cur.next
        self.insertAfter(cur)


def solve(part2=False):
    with open("input.txt", "r") as inputFile:
        root = None
        opSequence = []
        zeroNode = None
        deckey = 811589153
        prev = None
        for i, line in enumerate(inputFile.read().splitlines()):
            cur = Node(int(line) * (deckey if part2 else 1))
            if cur.n == 0:
                zeroNode = cur
            opSequence.append(cur)
            if i == 0:
                root = cur
            else:
                prev.next = cur
            cur.prev = prev
            prev = cur

        root.prev = cur
        cur.next = root

        listLenght = len(opSequence)
        for x in range(10 if part2 else 1):
            for node in opSequence:
                node.move(node.n % (listLenght - 1))
        cur = zeroNode
        ans = 0
        for x in range(3001):
            if x % 1000 == 0:
                ans += cur.n
            cur = cur.next
        print(ans)


solve()
solve(True)