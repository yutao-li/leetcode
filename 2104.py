from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        inf = float('inf')
        stack = [(-1, -inf)]
        arr = list(enumerate(nums)) + [(n, -inf)]
        for i, j in arr:
            while stack[-1][1] > j:
                a, b = stack.pop()
                res -= (a - stack[-1][0]) * (i - a) * b
            stack.append((i, j))
        stack = [(-1, inf)]
        arr = list(enumerate(nums)) + [(n, inf)]
        for i, j in arr:
            while stack[-1][1] < j:
                a, b = stack.pop()
                res += (a - stack[-1][0]) * (i - a) * b
            stack.append((i, j))
        return res


print(Solution().subArrayRanges(nums=[4, -2, -3, 4, 1]))
