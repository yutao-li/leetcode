from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(index, acc, path):
            if index >= len(candidates):
                return
            while acc < target:
                ori = path[:]
                helper(index + 1, acc, path)
                path = ori
                acc += candidates[index]
                path.append(candidates[index])
                if acc == target:
                    res.append(path[:])
                    return

        if not candidates:
            return []
        candidates.sort()
        res = []
        helper(0, 0, [])
        return res


print(Solution().combinationSum([2, 3, 5], 8))
