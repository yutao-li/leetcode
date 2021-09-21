from typing import List


class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        def traverse(front, part):
            i = front - 1
            while A[i] == 0:
                i -= 1
            zeros[part] = front - 1 - i
            j = i
            freq = 1
            while freq < count:
                i -= 1
                if A[i] == 1:
                    freq += 1
            return i, j

        if len(A) < 3:
            return [-1, -1]
        count = sum(A)
        if count == 0:
            return [0, 2]
        if count % 3:
            return [-1, -1]
        count /= 3
        zeros = [0] * 3

        i2, j2 = traverse(len(A), 2)
        i1, j1 = traverse(i2, 1)
        if zeros[2] > zeros[1] or j2 - i2 != j1 - i1:
            return [-1, -1]
        i0, j0 = traverse(i1, 0)
        if zeros[2] > zeros[0] or j1 - i1 != j0 - i0:
            return [-1, -1]
        if A[i0:j0] == A[i1:j1] == A[i2:j2]:
            return [j0 + zeros[2], j1 + 1 + zeros[2]]
        else:
            return [-1, -1]


print(Solution().threeEqualParts([1, 1, 0, 0, 1]))
