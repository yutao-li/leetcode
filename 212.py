from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, tree: dict):
            if board[r][c] in tree:
                child = tree[board[r][c]]
                if 0 in child:
                    res.append(child[0])
                    del child[0]
                if child:
                    pos = []
                    visited[r][c] = True
                    if r > 0:
                        pos.append((r - 1, c))
                    if c > 0:
                        pos.append((r, c - 1))
                    if r < len(board) - 1:
                        pos.append((r + 1, c))
                    if c < len(board[0]) - 1:
                        pos.append((r, c + 1))
                    for r1, c1 in pos:
                        if not visited[r1][c1]:
                            dfs(r1, c1, child)
                            if not child:
                                break
                    visited[r][c] = False
                if not child:
                    del tree[board[r][c]]

        trie = dict()
        for word in words:
            tmp = trie
            for ch in word:
                if ch not in tmp:
                    tmp[ch] = dict()
                tmp = tmp[ch]
            tmp[0] = word

        res = []
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie)
                if not trie:
                    return words
        return res


# board = [['a', 'a']]
# words = ['aa']
board = [["a", "b"], ["a", "a"]]
words = ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]
res = Solution().findWords(board, words)
