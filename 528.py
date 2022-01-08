from bisect import bisect_right
from random import randrange
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.acc = [0]
        for i in w:
            self.acc.append(self.acc[-1] + i)

    def pickIndex(self) -> int:
        return bisect_right(self.acc, randrange(self.acc[-1])) - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
