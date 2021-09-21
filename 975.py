from typing import List


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        next_h, next_l = [0] * n, [0] * n
        stack = []
        for _, i in sorted((j, i) for i, j in enumerate(A)):
            while stack and stack[-1] < i:
                next_h[stack.pop()] = i
            stack.append(i)
        stack = []
        for _, i in sorted((-j, i) for i, j in enumerate(A)):
            while stack and stack[-1] < i:
                next_l[stack.pop()] = i
            stack.append(i)
        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 2, -1, -1):
            higher[i] = lower[next_h[i]]
            lower[i] = higher[next_l[i]]
        return sum(higher)


res = Solution().oddEvenJumps([5, 1, 3, 4, 2])
