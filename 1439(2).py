from typing import List
import math
import heapq


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def dfs(acc, i, j):
            if i == j:
                return [acc + n for n in mat[i]]
            else:
                res = []
                for n in mat[i]:
                    res += dfs(acc + n, i + 1, j)
                return res

        j = math.ceil(math.log(k, len(mat[0])))
        if j == 0:
            return sum(row[0] for row in mat)
        else:
            res = sorted(dfs(0, 0, j - 1))[:k]
            for row in mat[j:]:
                heap = [(n + res[0], 0) for n in row[:k]]
                res1 = []
                for _ in range(k - 1):
                    s, i = heap[0]
                    res1.append(s)
                    heapq.heapreplace(heap, (s + res[i + 1] - res[i], i + 1))
                res1.append(heap[0][0])
                res = res1
            return res[-1]


res = Solution().kthSmallest([[1, 10, 10], [1, 4, 5], [2, 3, 6]], 14)
