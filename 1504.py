from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        height = [0] * len(mat[0])
        for row in mat:
            height = [height[i] + 1 if j else 0 for i, j in enumerate(row)]
            acc = [0] * len(mat[0])
            stack = []
            for i, j in enumerate(height):
                while stack and height[stack[-1]] > j:
                    stack.pop()
                acc[i] = acc[stack[-1]] + j * (i - stack[-1]) if stack else j * (i + 1)
                stack.append(i)
            res += sum(acc)
        return res


res = Solution().numSubmat([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
