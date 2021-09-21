import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left:
            self.left.append(-num)
        elif -self.left[0] < num:
            if len(self.right) > len(self.left):
                smallest = heapq.heappushpop(self.right, num)
                heapq.heappush(self.left, -smallest)
            else:
                heapq.heappush(self.right, num)
        else:
            if len(self.left) > len(self.right):
                largest = -heapq.heapreplace(self.left, -num)
                heapq.heappush(self.right, largest)
            else:
                heapq.heappush(self.left, -num)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(12)
obj.addNum(10)
obj.addNum(13)
obj.addNum(11)
obj.addNum(5)
print(obj.findMedian())
# param_2 = obj.findMedian()

