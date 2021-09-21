from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def divide(i, j):
            if i == j:
                return mat[i][:k]
            else:
                mid = (i + j) // 2
                l1 = divide(i, mid)
                l2 = divide(mid + 1, j)
                return sorted(a + b for a in l1 for b in l2)[:k]

        return divide(0, len(mat) - 1)[-1]


res = Solution().kthSmallest([[1, 3, 11], [2, 4, 6]], 5)
