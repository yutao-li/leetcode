from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = (1 << 9) - 1
        row_bitmap = [m] * 9
        col_bitmap = [m] * 9
        sq_bitmap = [[m] * 3 for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    bit = ~(1 << (int(board[i][j]) - 1))
                    row_bitmap[i] &= bit
                    col_bitmap[j] &= bit
                    sq_bitmap[i // 3][j // 3] &= bit

        def dfs(row, col):
            while row < 9 and board[row][col] != '.':
                col += 1
                if col == 9:
                    row += 1
                    col = 0
            if row == 9:
                return True
            r2, c2 = (row, col + 1) if col + 1 < 9 else (row + 1, 0)
            bitmap = row_bitmap[row] & col_bitmap[col] & sq_bitmap[row // 3][col // 3]
            while bitmap:
                n = bitmap & -bitmap
                bitmap &= ~n
                row_bitmap[row] &= ~n
                col_bitmap[col] &= ~n
                sq_bitmap[row // 3][col // 3] &= ~n
                board[row][col] = str(n.bit_length())
                if dfs(r2, c2):
                    return True
                row_bitmap[row] |= n
                col_bitmap[col] |= n
                sq_bitmap[row // 3][col // 3] |= n
            board[row][col] = '.'
            return False

        dfs(0, 0)


res = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
       [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
       ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
       [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
Solution().solveSudoku(res)
