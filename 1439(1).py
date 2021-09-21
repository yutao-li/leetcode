from typing import List
import heapq


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        res = mat[0][:k]
        for row in mat[1:]:
            heap = [(n + row[0], 0) for n in res]
            res = []
            for _ in range(k):
                if not heap:
                    break
                s, i = heap[0]
                res.append(s)
                if i == len(mat[0]) - 1:
                    heapq.heappop(heap)
                else:
                    heapq.heapreplace(heap, (s + row[i + 1] - row[i], i + 1))
        return res[-1]


res = Solution().kthSmallest([[1, 10, 10], [1, 4, 5], [2, 3, 6]], 14)
