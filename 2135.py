from functools import reduce
from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        b = ord('a')
        seen = set()
        for s in startWords:
            r = reduce(lambda a, b: a | b, (1 << (ord(ch) - b) for ch in s))
            for i in range(26):
                ch = 1 << i
                if not r & ch:
                    seen.add(r | ch)
        return sum(sum(1 << (ord(ch) - b) for ch in t) in seen for t in targetWords)
