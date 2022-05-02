from math import ceil, floor


def findOptimalButtonPress(pressCost, moveCost, gapCost, desiredTime):
    def getSeconds(sequence):
        minute, second = divmod(sequence, 100)
        return minute * 60 + second

    def getCost(sequence):
        buttons = []
        while sequence:
            sequence, curButton = divmod(sequence, 10)
            buttons.append(curButton)
        cost = len(buttons) * pressCost
        cost += sum(i != j for i, j in zip(buttons, buttons[1:])) * moveCost
        return cost

    def getRangeOfSequence(low, high):
        lminute, lsecond = divmod(low, 60)
        if lsecond < 40 and lminute > 0:
            lminute -= 1
            lsecond += 60
        hminute, hsecond = divmod(high, 60)
        return lminute * 100 + lsecond, hminute * 100 + hsecond

    desiredTime = getSeconds(int(desiredTime))
    low = ceil(desiredTime * 0.9)
    high = floor(desiredTime * 1.1)
    optimal = [float('inf')] * 3
    lbound, hbound = getRangeOfSequence(low, high)
    for sequence in range(lbound, hbound + 1):
        curTime = getSeconds(sequence)
        if low <= curTime <= high:
            cost = getCost(sequence)
            timeGap = abs(curTime - desiredTime)
            if timeGap > desiredTime * 0.05:
                cost += gapCost
            if optimal[0] > cost or optimal[0] == cost and timeGap < optimal[1]:
                optimal = [cost, timeGap, sequence]
    return str(optimal[2])


print(findOptimalButtonPress(1, 2, 2, 1000))
