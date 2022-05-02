from asyncio import Future
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from typing import List


class Solution:
    def mergeNLists(self, lists: [[int]], nThreads: int) -> List[int]:
        def merge(l1: [int], l2: [int]) -> [int]:
            res = []
            i1 = 0
            i2 = 0
            n1 = len(l1)
            n2 = len(l2)
            while i1 < n1 and i2 < n2:
                if l1[i1] < l2[i2]:
                    res.append(l1[i1])
                    i1 += 1
                else:
                    res.append(l2[i2])
                    i2 += 1
            if i1 < n1:
                res += l1[i1:]
            elif i2 < n2:
                res += l2[i2:]
            return res

        n = len(lists)
        with ThreadPoolExecutor(max_workers=nThreads) as executor:
            tasks = deque()
            for li in lists:
                f = Future()
                f.set_result(li)
                tasks.append(f)
            for _ in range(n - 1):
                tasks.append(executor.submit(merge, tasks.popleft().result(), tasks.popleft().result()))
        return tasks.popleft().result()


print(Solution().mergeNLists([[1, 2, 4], [3, 5], [2, 8, 10]], 10))
