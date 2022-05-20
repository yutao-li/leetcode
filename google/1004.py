class RunLengthDecoder:
    def __init__(self, runLength):
        if not runLength:
            raise ValueError('empty input')
        if len(runLength) % 2:
            raise ValueError('run length input has odd length ' + str(len(runLength)))
        self.runLength = runLength[::-1]

    def hasNext(self):
        while self.runLength and self.runLength[-1] <= 0:
            self.runLength.pop()
            self.runLength.pop()
        return bool(self.runLength)

    def __next__(self):
        if not self.hasNext():
            raise StopIteration('no element remains')
        self.runLength[-1] -= 1
        return self.runLength[-2]


runLengthDecoder = RunLengthDecoder([1, 2, 0, 8, 3, 4])
for _ in range(4):
    print(next(runLengthDecoder))
