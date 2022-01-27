from collections import defaultdict
from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.pos = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.pos[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        arr1 = self.pos[word1]
        arr2 = self.pos[word2]
        if arr1[0] > arr2[0]:
            arr1, arr2 = arr2, arr1
        n1 = len(arr1)
        n2 = len(arr2)
        i1 = i2 = 0
        res = arr2[0] - arr1[0]
        while i1 < n1 and i2 < n2 and res > 1:
            while i1 + 1 < n1 and arr1[i1 + 1] < arr2[i2]:
                i1 += 1
            res = min(res, arr2[i2] - arr1[i1])
            i1 += 1
            if i1 < n1:
                while i2 + 1 < n2 and arr2[i2 + 1] < arr1[i1]:
                    i2 += 1
                res = min(res, arr1[i1] - arr2[i2])
                i2 += 1
        return res


# Your WordDistance object will be instantiated and called as such:
obj = WordDistance(["a", "c", "b", "b", "a"])
param_1 = obj.shortest('a', 'b')
