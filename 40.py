from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(index, acc, path):
            if acc == target:
                res.append(path[:])
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if acc + candidates[i] > target:
                    break
                path.append(candidates[i])
                helper(i + 1, acc + candidates[i], path)
                path.pop()

        if not candidates:
            return []
        candidates.sort()
        res = []
        helper(0, 0, [])
        return res


print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
