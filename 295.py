from bisect import insort


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.li = []

    def addNum(self, num: int) -> None:
        insort(self.li, num)

    def findMedian(self) -> float:
        q, r = divmod(len(self.li), 2)
        if r:
            return self.li[q]
        else:
            return (self.li[q] + self.li[q - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
