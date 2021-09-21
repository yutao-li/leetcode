from typing import List
from collections import defaultdict


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def dfs(index):
            transfer = float('inf')
            while index < len(balance) and balance[index] == 0:
                index += 1
            if index == len(balance):
                return 0
            prev = 0
            for i, j in enumerate(balance[pos:], start=pos):
                if j != prev and j * balance[index] < 0:
                    prev = j
                    balance[i] += balance[index]
                    transfer = min(transfer, 1 + dfs(index + 1))
                    balance[i] -= balance[index]
            return transfer

        balance = defaultdict(int)
        for a, b, c in transactions:
            balance[a] -= c
            balance[b] += c
        balance = sorted(i for i in balance.values() if i != 0)
        if not balance:
            return 0
        pos = 0
        while balance[pos] < 0:
            pos += 1
        return dfs(0)


res = Solution().minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]])
