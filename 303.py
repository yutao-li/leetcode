from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.acc = [0]
        for num in nums:
            self.acc.append(num + self.acc[-1])

    def sumRange(self, i: int, j: int) -> int:
        return self.acc[j + 1] - self.acc[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
