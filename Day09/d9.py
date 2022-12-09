def moveTail(tail, head):
    distance = lambda a, b: (a.real - b.real)**2 + (a.imag - b.imag)**2
    if tail == head or distance(tail, head) <= 2:
        return tail
    if tail.real == head.real or tail.imag == head.imag:
        if abs(tail.real - head.real) == 2:
            return tail + (-1 if (tail.real > head.real) else 1)
        if abs(tail.imag - head.imag) == 2:
            return tail + (-1j if (tail.imag > head.imag) else 1j)

    dx, dy = head.real - tail.real, head.imag - tail.imag
    return tail + (1 if dx > 0 else -1) + (1j if dy > 0 else -1j)


def solve(input, knots):
    commands = {'R': 1, 'U': 1j, 'D': -1j, 'L': -1}
    tailPositions = set()
    tailPositions.add(knots[-1])
    for cmd in input:
        direction, step = cmd.split(' ')
        for _ in range(int(step)):
            knots[0] += commands[direction]
            for i in range(1, len(knots)):
                knots[i] = moveTail(knots[i], knots[i - 1])
            tailPositions.add(knots[-1])
    return len(tailPositions)


with open("input.txt", "r") as inputFile:
    input = inputFile.read().splitlines()
    print(solve(input, [0j, 0j]))
    print(solve(input, [0j for _ in range(10)]))