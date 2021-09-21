from typing import List
from bisect import bisect_right, bisect_left


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if m == 1:
            return sum(nums)
        acc = [0]
        for n in nums:
            acc.append(acc[-1] + n)
        low = sum(nums) // m
        high = low
        i = 0
        bound = low
        for _ in range(m - 1):
            i = bisect_left(acc, bound, i)
            if i == len(acc):
                break
            high = max(high, acc[i] + low - bound)
            bound = acc[i] + low
            i += 1
        while low < high:
            mid = (low + high) // 2
            i = 0
            bound = mid
            for _ in range(m):
                i = bisect_right(acc, bound, i)
                bound = acc[i - 1] + mid
            if i == len(acc):
                high = mid
            else:
                low = mid + 1
        return high


res = Solution().splitArray([7, 2, 5, 10, 8], 2)
