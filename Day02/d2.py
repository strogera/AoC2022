outcomeScore = {
    ('A', 'A'): 1 + 3,
    ('A', 'B'): 2 + 6,
    ('A', 'C'): 3 + 0,
    ('B', 'A'): 1 + 0,
    ('B', 'B'): 2 + 3,
    ('B', 'C'): 3 + 6,
    ('C', 'A'): 1 + 6,
    ('C', 'B'): 2 + 0,
    ('C', 'C'): 3 + 3
}
userShape1 = {'X': 'A', 'Y': 'B', 'Z': 'C'}
userShape2 = {
    ('A', 'X'): 'C',
    ('A', 'Y'): 'A',
    ('A', 'Z'): 'B',
    ('B', 'X'): 'A',
    ('B', 'Y'): 'B',
    ('B', 'Z'): 'C',
    ('C', 'X'): 'B',
    ('C', 'Y'): 'C',
    ('C', 'Z'): 'A'
}

getScore1 = lambda a, b: outcomeScore[a, userShape1[b]]
getScore2 = lambda a, b: outcomeScore[a, userShape2[(a, b)]]

with open("input.txt", "r") as inputFile:
    play = [(x, y) for x, y in (line.strip().split(' ') for line in inputFile.readlines())]
    print(sum(getScore1(x, y) for x, y in play))
    print(sum(getScore2(x, y) for x, y in play))