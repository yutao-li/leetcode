from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, path, row, col):
            if i == len(word):
                return True
            pos = []
            if row > 0:
                pos.append((row - 1, col))
            if row < len(board) - 1:
                pos.append((row + 1, col))
            if col > 0:
                pos.append((row, col - 1))
            if col < len(board[0]) - 1:
                pos.append((row, col + 1))
            for r, c in pos:
                if (r, c) not in path and board[r][c] == word[i]:
                    path.add((r, c))
                    res = dfs(i + 1, path, r, c)
                    if res:
                        return True
                    path.remove((r, c))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(1, {(i, j)}, i, j):
                        return True
        return False


board = [
    ['a', 'a']
]
res = Solution().exist(board, 'aaa')
