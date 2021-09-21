from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        aver, r = divmod(sum(machines), len(machines))
        if r:
            return -1
        res = 0
        i = 0
        last_m = 0
        while i < len(machines) - 1:
            move = aver - machines[i]
            machines[i + 1] -= move
            res = max(res, abs((move - last_m) if move < 0 < last_m else move))
            last_m = move
            i += 1
        return res


print(Solution().findMinMoves([44, 46, 11, 2, 12, 64, 40, 60, 92, 9]))
