from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(p)
        n2 = len(s)
        if n1 > n2:
            return []
        res = []
        c1 = Counter(p)
        c2 = Counter(s[:n1])
        for k, v in c1.items():
            c2[k] -= v
        zero = sum(v == 0 for v in c2.values())
        n3 = len(c2)
        if zero == n3:
            res.append(0)
        i = n1
        while i < n2:
            c2[s[i]] += 1
            v = c2[s[i]]
            if v == 0:
                zero += 1
            elif v == 1:
                zero -= 1
            c2[s[i - n1]] -= 1
            v = c2[s[i - n1]]
            if v == 0:
                zero += 1
            elif v == -1:
                zero -= 1
            if zero == n3:
                res.append(i - n1 + 1)
            i += 1
        return res


res = Solution().findAnagrams(s="abab", p="ab")

