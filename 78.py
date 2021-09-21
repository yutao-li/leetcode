from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(1, 1 << len(nums)):
            s = []
            for n in nums:
                i, r = divmod(i, 2)
                if r:
                    s.append(n)
                if i == 0:
                    break
            res.append(s)
        return res


res = Solution().subsets([1, 2, 3])
