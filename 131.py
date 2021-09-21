from typing import List
from string import ascii_lowercase


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        ordinal = dict(zip(ascii_lowercase, range(26)))
        res = []
        queue = [[0]]
        modulus = 2 ** 63 - 1
        while queue:
            li = queue.pop()
            i = li[-1]
            forward = ordinal[s[i]]
            backward = ordinal[s[i]]
            power = 26
            i += 1
            while i < len(s):
                if forward == backward:
                    queue.append(li + [i])
                forward = (forward * 26 + ordinal[s[i]]) % modulus
                backward = (ordinal[s[i]] * power + backward) % modulus
                power *= 26
                i += 1
            if forward == backward:
                par = []
                for i in range(1, len(li)):
                    par.append(s[li[i - 1]:li[i]])
                par.append(s[li[-1]:])
                res.append(par)
        return res


print(Solution().partition('a'))
