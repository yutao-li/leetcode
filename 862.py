from typing import List
from collections import deque


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        if not A:
            return -1
        acc = [0]
        for i in A:
            acc.append(acc[-1] + i)
        q = deque()
        res = len(A) + 1
        for i in range(len(acc)):
            while q and acc[i] - acc[q[0]] >= K:
                res = min(res, i - q.popleft())
            while q and acc[q[-1]] > acc[i]:
                q.pop()
            q.append(i)
        return res if res != len(A) + 1 else -1


print(Solution().shortestSubarray([1, 2], 4))
