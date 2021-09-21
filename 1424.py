from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        size = max(i + len(row) for i, row in enumerate(nums))
        dist = [[] for _ in range(size)]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                dist[i + j].append(nums[i][j])
        for row in dist:
            res += row[::-1]
        return res


res = Solution().findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]])
