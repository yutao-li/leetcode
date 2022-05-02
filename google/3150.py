from collections import deque


class Clock:
    def __init__(self):
        self.timestamp = 0

    def getTime(self):
        return self.timestamp

    def incrementTime(self, duration):
        self.timestamp += duration


class TemperatureTracker:
    def __init__(self, clock):
        self.clock = clock
        self.tempStack = deque()

    def getMaxTemperature(self):
        now = self.clock.getTime()
        while self.tempStack and self.tempStack[0][1] + 24 < now:
            self.tempStack.popleft()
        if not self.tempStack:
            raise ValueError('no temperatures recorded in last 24 hours')
        return self.tempStack[0][0]

    def registerTemperature(self, temperature):
        while self.tempStack and self.tempStack[-1][0] < temperature:
            self.tempStack.pop()
        now = self.clock.getTime()
        self.tempStack.append((temperature, now))
