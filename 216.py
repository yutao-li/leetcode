from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        res = []

        def helper(index, acc, path):
            if len(path) == k:
                if acc == n:
                    res.append(path[:])
                return
            for i in range(index, len(candidates)):
                if acc + candidates[i] > n:
                    break
                path.append(candidates[i])
                helper(i + 1, acc + candidates[i], path)
                path.pop()

        helper(0, 0, [])
        return res


print(Solution().combinationSum3(3, 9))
