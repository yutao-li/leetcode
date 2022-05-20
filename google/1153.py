class Image:
    def getColor(self, x, y) -> str:
        pass

    def isValid(self, x, y) -> bool:
        pass


around = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]
neighbour = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def getSurroundPixels(x, y):
    return [(x + dx, y + dy) for dx, dy in around]


def getAdjPixels(x, y):
    return [(x + dx, y + dy) for dx, dy in neighbour]


def getSurroundWaters(x, y, image):
    def search(x, y):
        seen.add((x, y))
        for x1, y1 in getSurroundPixels(x, y):
            if image.isValid(x1, y1) and image.getColor(x1, y1) == 'green':
                if (x1, y1) not in seen:
                    search(x1, y1)
            else:
                waters.add((x1, y1))

    seen = set()
    waters = set()
    search(x, y)
    return waters


def findNumOfLakes(waters):
    def connectWaters(x, y):
        seen.add((x, y))
        for x1, y1 in getAdjPixels(x, y):
            if (x1, y1) in waters and (x1, y1) not in seen:
                connectWaters(x1, y1)

    num = 0
    seen = set()
    for x, y in waters:
        if (x, y) not in seen:
            num += 1
            connectWaters(x, y)
    return num - 1


def countLakes(image, x, y):
    if not image.isValid(x, y):
        return -1
    if image.getColor(x, y) == 'blue':
        return -1
    waters = getSurroundWaters(x, y, image)
    return findNumOfLakes(waters)
