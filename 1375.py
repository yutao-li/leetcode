from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        left = 1
        on = 0
        res = 0
        for i, j in enumerate(light, start=1):
            on |= 1 << j
            while on & (1 << left):
                left += 1
            if left == i + 1:
                res += 1
        return res


res = Solution().numTimesAllBlue(light=[3, 2, 4, 1, 5])
