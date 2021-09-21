from collections import defaultdict
from math import sqrt


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if N == 1:
            return 1
        factor = defaultdict(int)
        divided = True
        while divided:
            divided = False
            for i in range(2, int(sqrt(N)) + 1):
                q, r = divmod(N, i)
                if r == 0:
                    divided = True
                    N = q
                    factor[i] += 1
                    break
        factor[N] += 1
        res = 1
        factor[2] = 0
        for i in factor.values():
            res *= i + 1
        return res


res = Solution().consecutiveNumbersSum(15)
