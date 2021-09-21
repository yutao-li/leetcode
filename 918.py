from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        t_sum = 0
        res = float('-inf')
        for num in A:
            t_sum += num
            res = max(res, t_sum)
            if t_sum < 0:
                t_sum = 0
        acc = [A[0]]
        for i in A[1:]:
            acc.append(acc[-1] + i)
        r_best = []
        t_sum = 0
        res1 = float('-inf')
        for num in A[::-1]:
            t_sum += num
            res1 = max(res1, t_sum)
            r_best.append(res1)
        return max(res, max((acc[i] + r_best[len(A) - i - 2] for i in range(len(A) - 1)), default=float('-inf')))


print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))
