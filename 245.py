from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word1 == word2:
            arr = [i for i, j in enumerate(wordsDict) if j == word1]
            return min(j - i for i, j in zip(arr, arr[1:]))
        else:
            pos = []
            for i, word in enumerate(wordsDict):
                if word == word1:
                    pos.append((i, 0))
                elif word == word2:
                    pos.append((i, 1))
            return min(i2 - i1 for (i1, j1), (i2, j2) in zip(pos, pos[1:]) if j1 != j2)
