with open("input.txt", "r") as inputFile:
    input = [list(map(int, x.replace('-', ',').split(','))) for x in inputFile.read().splitlines()]
    count = count2 = 0
    for a, b, x, y in input:
        if (a >= x and b <= y) or (x >= a and y <= b):
            count += 1
            count2 += 1
        elif (a <= x <= b) or (a <= y <= b):
            count2 += 1
    print(count)
    print(count2)