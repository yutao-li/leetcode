from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos = []
        for i, word in enumerate(wordsDict):
            if word == word1:
                pos.append((i, 0))
            elif word == word2:
                pos.append((i, 1))
        return min(i2 - i1 for (i1, j1), (i2, j2) in zip(pos, pos[1:]) if j1 != j2)
