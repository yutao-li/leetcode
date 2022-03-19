from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = Counter(s)
        res = []
        for ch in order:
            if ch in s:
                res.append(ch * s[ch])
                del s[ch]
        res += [k * v for k, v in s.items()]
        return ''.join(res)


print(Solution().customSortString(order="cba", s="abcd"))
