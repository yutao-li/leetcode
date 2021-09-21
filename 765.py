from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        row = [i // 2 for i in row]
        pos = [0] * len(row)
        for i in range(len(row) - 1, -1, -1):
            pos[row[i]] = i
        swap = 0
        while row:
            i = row[-1]
            j = row[-2]
            if i != j:
                swap += 1
                if pos[i] > pos[j]:
                    row[pos[i]] = j
                else:
                    row[pos[j]] = i
            row.pop()
            row.pop()
        return swap


print(Solution().minSwapsCouples([3, 2, 0, 1]))
