from typing import List
from collections import defaultdict
from random import randrange


class Solution:

    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for i, n in enumerate(nums):
            self.d[n].append(i)

    def pick(self, target: int) -> int:
        indices = self.d[target]
        return indices[randrange(len(indices))]


class Solution1:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        idx = -1
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1
                if randrange(count) == 0:
                    idx = i
        return idx
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
