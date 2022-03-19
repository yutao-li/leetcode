class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = []
        self.acc = 0
        self.ptr = 0

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
            self.acc += val
            return self.acc / len(self.window)
        else:
            self.acc += val - self.window[self.ptr]
            self.window[self.ptr] = val
            self.ptr += 1
            if self.ptr == self.size:
                self.ptr = 0
            return self.acc / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
