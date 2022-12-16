manhattanDistance = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class Sensor:

    def __init__(self, sensor, beacon):
        self.sensor = sensor
        self.beacon = beacon
        distance = manhattanDistance(sensor, beacon)
        self.distance = distance
        self.rombusTop = sensor[1] - distance
        self.rombusBottom = sensor[1] + distance
        self.rombusLeft = sensor[0] - distance
        self.rombusRight = sensor[0] + distance

    def isInSensorArea(self, point):
        return self.distance >= manhattanDistance(self.sensor, point)

    def getMaxXRange(self):
        return range(self.rombusLeft, self.rombusRight + 1)

    def getExternalPoints(self):
        x = self.rombusLeft
        y = self.sensor[1]
        while x <= self.sensor[0] and y >= self.rombusTop:
            yield (x - 1, y)
            x += 1
            y -= 1
        x = self.sensor[0]
        y = self.rombusTop
        while x <= self.rombusRight and y <= self.sensor[1]:
            yield (x, y - 1)
            x += 1
            y += 1
        x = self.rombusRight
        y = self.sensor[1]
        while x >= self.sensor[0] and y <= self.rombusBottom:
            yield (x + 1, y)
            x -= 1
            y += 1

        x = self.sensor[0]
        y = self.rombusBottom
        while x >= self.rombusLeft and y >= self.sensor[1]:
            yield (x, y + 1)
            x -= 1
            y -= 1

with open("input.txt", "r") as inputFile:
    sensors = []
    for line in inputFile.read().splitlines():
        l = line.split(' ')
        x = int(l[2][:-1].split('=')[1])
        y = int(l[3][:-1].split('=')[1])
        bx = int(l[-2][:-1].split('=')[1])
        by = int(l[-1].split('=')[1])
        sensors.append(Sensor((x, y), (bx, by)))

    y = 2000000
    ans = set()
    for s in sensors:
        for x in s.getMaxXRange():
            if s.isInSensorArea((x, y)) and (x, y) != s.beacon:
                ans.add((x, y))
    print(len(ans))
    maxx = 4_000_000 
    for s1 in sensors:
        for c in s1.getExternalPoints():
            if not(0<=c[0]<=maxx and 0<=c[1]<=maxx):
                continue
            found = True
            for s2 in sensors:
                if s2.isInSensorArea(c):
                    found = False
                    break
            if found == True:
                x, y = c
                print(x * maxx + y)
                exit()