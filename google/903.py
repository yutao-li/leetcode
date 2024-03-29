from math import ceil, floor


class MicroWave:
    def __init__(self, pressCost, moveCost, gapCost):
        def getSeconds(sequence):
            minute, second = divmod(sequence, 100)
            return minute * 60 + second

        def getMovesAndPress(sequence):
            sequence = str(sequence)
            return sum(i != j for i, j in zip(sequence, sequence[1:])), len(sequence)

        self.pressCost = pressCost
        self.moveCost = moveCost
        self.gapCost = gapCost
        self.seq2sec = [getSeconds(i) for i in range(10000)]
        self.seq2movesAndPress = [getMovesAndPress(i) for i in range(10000)]

    def findOptimalButtonPress(self, desiredTime):
        def getCost(sequence):
            moves, press = self.seq2movesAndPress[sequence]
            return press * pressCost + moves * moveCost

        def getRangeOfSequence(low, high):
            lminute, lsecond = divmod(low, 60)
            if lsecond < 40 and lminute > 0:
                lminute -= 1
                lsecond += 60
            hminute, hsecond = divmod(high, 60)
            return lminute * 100 + lsecond, hminute * 100 + hsecond

        pressCost, moveCost, gapCost = self.pressCost, self.moveCost, self.gapCost
        desiredTime = self.seq2sec[int(desiredTime)]
        low = ceil(desiredTime * 0.9)
        high = floor(desiredTime * 1.1)
        optimal = [float('inf')] * 3
        lbound, hbound = getRangeOfSequence(low, high)
        for sequence in range(lbound, hbound + 1):
            curTime = self.seq2sec[sequence]
            if low <= curTime <= high:
                cost = getCost(sequence)
                timeGap = abs(curTime - desiredTime)
                if timeGap > desiredTime * 0.05:
                    cost += gapCost
                if optimal[0] > cost or optimal[0] == cost and timeGap < optimal[1]:
                    optimal = [cost, timeGap, sequence]
        return str(optimal[2])


print(MicroWave(1, 2, 2).findOptimalButtonPress(1000))
