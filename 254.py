from typing import List
from functools import cache
from math import sqrt


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        @cache
        def factorize(n, start):
            res = []
            for i in range(start, int(sqrt(n)) + 1):
                q, r = divmod(n, i)
                if r == 0:
                    res1 = factorize(q, i)
                    res += [[i] + j for j in res1]
            res.append([n])
            return res

        if n == 1:
            return []
        res = factorize(n, 2)
        res.pop()
        return res


class Solution1:
    def getFactors(self, n):
        todo, combis = [(n, 2, [])], []
        while todo:
            n, i, combi = todo.pop()
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n / i],
                    todo += (n / i, i, combi + [i]),
                i += 1
        return combis


print(Solution().getFactors(12))
