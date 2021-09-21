from typing import List


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        A.sort()
        aver = sum(A) / len(A)
        if len(A) == 1:
            return False
        if A[0] == aver:
            return True
        num = len(A) // 2
        pool = {(0, 0), (A[0], 1)}
        for i in A[1:]:
            for su, n in list(pool):
                if n < num:
                    av = (su + i) / (n + 1)
                    if av == aver:
                        return True
                    elif av < aver:
                        pool.add((su + i, n + 1))
                    else:
                        pool.remove((su, n))
        return False


print(Solution().splitArraySameAverage([3, 1]))
