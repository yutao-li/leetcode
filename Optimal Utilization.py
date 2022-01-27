# https://leetcode.com/discuss/interview-question/373202
from collections import defaultdict
from typing import List


class Solution:
    def getPairs(self, a: List[List[int]], b: List[List[int]], target: int) -> List[List[int]]:
        a1 = defaultdict(list)
        for i, j in a:
            a1[j].append(i)
        b1 = defaultdict(list)
        for i, j in b:
            b1[j].append(i)
        i2 = 0
        v1 = sorted(a1.keys())
        v2 = sorted(b1.keys())
        if v1[0] + v2[0] > target:
            return []
        while i2 + 1 < len(b) and v1[0] + v2[i2 + 1] <= target:
            i2 += 1
        s = v1[0] + v2[i2]
        res = [[i, j] for i in a1[v1[0]] for j in b1[v2[i2]]]
        for v in v1[1:]:
            while v + v2[i2] > target and i2 > 0:
                i2 -= 1
            s1 = v + v2[i2]
            if s1 > target:
                return res
            if s == s1:
                res += [[i, j] for i in a1[v] for j in b1[v2[i2]]]
            elif s < s1:
                s = s1
                res = [[i, j] for i in a1[v] for j in b1[v2[i2]]]
        return res


print(Solution().getPairs(a=[[1, 2], [2, 4], [3, 6]],
                          b=[[1, 2]],
                          target=7))

print(Solution().getPairs(a=[[1, 3], [2, 5], [3, 7], [4, 10]],
                          b=[[1, 2], [2, 3], [3, 4], [4, 5]],
                          target=10))

print(Solution().getPairs(a=[[1, 8], [2, 7], [3, 14]],
                          b=[[1, 5], [2, 10], [3, 14]],
                          target=20))

print(Solution().getPairs(a=[[1, 8], [2, 15], [3, 9]],
                          b=[[1, 8], [2, 11], [3, 12]],
                          target=20))
