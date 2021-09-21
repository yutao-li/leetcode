from collections import Counter
from math import factorial


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        prod = 1
        c = Counter(tiles)
        for v in c.values():
            prod *= v + 1
        res = 0
        for i in range(1, prod):
            nums = []
            for v in c.values():
                i, r = divmod(i, v + 1)
                if r:
                    nums.append(r)
                if i == 0:
                    break
            num = factorial(sum(nums))
            for j in nums:
                num //= factorial(j)
            res += num
        return res

res=Solution().numTilePossibilities('AAABBC')
