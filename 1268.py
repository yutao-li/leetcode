from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        n = len(searchWord)
        res = [[] for _ in range(n)]
        for p in products:
            i = 0
            max_length = min(len(p), n)
            while i < max_length and searchWord[i] == p[i]:
                if len(res[i]) < 3:
                    res[i].append(p)
                i += 1
        return res
