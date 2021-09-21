from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(i, acc):
            acc1 = nums[i] + acc
            if acc1 < target:
                return i + 1 < len(nums) and (dfs(i + 1, acc1) or dfs(i + 1, acc))
            elif acc1 == target:
                return True
            else:
                return False

        target, r = divmod(sum(nums), 2)
        if r:
            return False
        nums.sort(reverse=True)
        return dfs(0, 0)


res = Solution().canPartition([1, 2, 3, 5])

