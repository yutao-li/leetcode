from typing import List


class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        m = 10 ** 9 + 7
        n = len(nums)
        res = 0
        inf = float('inf')
        stack = [(-1, -inf)]
        arr = list(enumerate(nums)) + [(n, -inf)]
        for i, j in arr:
            while stack[-1][1] > j:
                a, b = stack.pop()
                res = (res + (a - stack[-1][0]) * (i - a) * b) % m
            stack.append((i, j))
        return res
