def findIndexDigitMatch(pi):
    piWindow = ''
    for i in range(1, 10 ** 6 + 1):
        iStr = str(i)
        piWindow += str(next(pi))
        if len(piWindow) > len(iStr):
            piWindow = piWindow[1:]
        if piWindow == iStr:
            print(i)


def findIndexDigitMatch1(pi):
    piSlice = 0
    modulo = 10
    for i in range(1, 10 ** 6 + 1):
        if i >= modulo:
            modulo *= 10
        piSlice = (10 * piSlice + next(pi)) % modulo
        if piSlice == i:
            print(i)


pi = [3, 1, 4, 1, 5, 9, 2, 6, 5, 1, 0, 1, 3, 4]
# findIndexDigitMatch(iter(pi))
findIndexDigitMatch1(iter(pi))
