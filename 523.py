from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = set()
        remainders.add(0)
        acc = nums[0]
        pre_acc = 0
        for num, pre_num in zip(nums[1:], nums):
            acc = (acc + num) % k
            if acc in remainders:
                return True
            pre_acc = (pre_acc + pre_num) % k
            remainders.add(pre_acc)
        return False
