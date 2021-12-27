from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        hori = dict()
        vert = dict()
        virtual_initial_row, virtual_initial_col = 0, 0
        res = [0] * len(s)
        r, c = startPos
        for i in range(len(s) - 1, -1, -1):
            hori[virtual_initial_row] = i
            vert[virtual_initial_col] = i
            if s[i] == 'L':
                virtual_initial_col += 1
            elif s[i] == 'R':
                virtual_initial_col -= 1
            elif s[i] == 'U':
                virtual_initial_row += 1
            else:
                virtual_initial_row -= 1
            row_gap, col_gap = r - virtual_initial_row, c - virtual_initial_col
            step = len(s) - i
            if -row_gap - 1 in hori:
                step = min(step, hori[-row_gap - 1] - i)
            if -row_gap + n in hori:
                step = min(step, hori[-row_gap + n] - i)
            if -col_gap - 1 in vert:
                step = min(step, vert[-col_gap - 1] - i)
            if -col_gap + n in vert:
                step = min(step, vert[-col_gap + n] - i)
            res[i] = step
        return res


print(Solution().executeInstructions(n=1, startPos=[0, 0], s="LRUD"))
