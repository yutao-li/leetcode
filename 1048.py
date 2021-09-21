from typing import List
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def dfs(w):
            res = 1
            if len(w) - 1 in sw:
                for i in range(len(w)):
                    w1 = w[:i] + w[i + 1:]
                    if w1 in sw[len(w) - 1]:
                        sw[len(w) - 1].remove(w1)
                        res = max(res, 1 + dfs(w1))
            return res

        sw = defaultdict(set)
        for w in words:
            sw[len(w)].add(w)
        minlen = min(sw)
        res = 1
        for l in sorted(sw, reverse=True):
            if l - minlen < res:
                break
            for w in sw[l]:
                res = max(res, dfs(w))
        return res
