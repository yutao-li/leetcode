from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = [0] + nums
        power = 2
        while power < len(self.bit):
            i = 1
            while i * power < len(self.bit):
                self.bit[i * power] += self.bit[i * power - power // 2]
                i += 1
            power *= 2

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        i = i + 1
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def sumRange(self, i: int, j: int) -> int:
        def sum(i: int):
            res = 0
            while i:
                res += self.bit[i]
                i -= i & (-i)
            return res

        return sum(j + 1) - sum(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
