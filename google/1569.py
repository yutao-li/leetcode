class Landscape:
    allDirections = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

    def __init__(self, row, column):
        self.row = row + 2
        self.column = column + 2
        self.parent = [-1] * (self.row * self.column)
        for i in range(self.row):
            self.parent[self.getIndex(i, 0)] = 0
            self.parent[self.getIndex(i, self.column - 1)] = 0
        for i in range(self.column):
            self.parent[self.getIndex(0, i)] = 0
            self.parent[self.getIndex(self.row - 1, i)] = 0
        self.numWaters = 1

    def getIndex(self, x, y) -> int:
        return x * self.column + y

    def fill(self, x, y) -> int:
        x += 1
        y += 1
        index = self.getIndex(x, y)
        if self.parent[index] >= 0:
            return self.numWaters
        self.parent[index] = index
        self.numWaters -= 1
        neighbours = [self.getIndex(x + i, y + j) for i, j in Landscape.allDirections]
        parentsOfNeighbours = [self.getParent(i) for i in neighbours] * 2
        waters = [i for i in range(0, 8, 2) if parentsOfNeighbours[i] == -1]
        for i in range(len(waters)):
            w1 = waters[i]
            if w1 == -1:
                continue
            self.numWaters += 1
            for j in range(i + 1, len(waters)):
                w2 = waters[j]
                if w2 == -1:
                    continue
                connected = True
                for k in range(w1 + 1, w2):
                    if parentsOfNeighbours[k] >= 0 and parentsOfNeighbours[k] in parentsOfNeighbours[w2 + 1:w1 + 8]:
                        connected = False
                        break
                if connected:
                    waters[j] = -1
        for parent in parentsOfNeighbours[:8]:
            if parent >= 0:
                self.parent[parent] = index
        return self.numWaters

    def getParent(self, index):
        if self.parent[index] == -1:
            return -1
        while self.parent[index] != index:
            self.parent[index] = self.parent[self.parent[index]]
            index = self.parent[index]
        return index


landscape = Landscape(3, 3)
print(landscape.fill(0, 1))
print(landscape.fill(2, 1))
print(landscape.fill(1, 1))
print(landscape.fill(1, 2))
