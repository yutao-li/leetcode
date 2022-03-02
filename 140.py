from functools import lru_cache
from typing import List


class Solution:
    class Node:
        def __init__(self, w=False):
            self.w = w
            self.next = {}

    class Trie:
        def __init__(self):
            self.root = Solution.Node(False)
            self.memoization = {}

        def put(self, word):
            self.auxput(word, 0, self.root)

        def auxput(self, word, d, node):
            if d == len(word):
                node.w = True
            else:
                if word[d] not in node.right:
                    node.right[word[d]] = Solution.Node()
                self.auxput(word, d + 1, node.right[word[d]])

    def dfs(self, s, index, node, trie):
        if index == len(s):
            if node.w:
                return [[len(s)]]
            return []
        else:
            result = []
            if node.w:
                if index in trie.memoization:
                    result = trie.memoization[index]
                else:
                    result = self.dfs(s, index, trie.root, trie)
                    trie.memoization[index] = result
                result = [[index] + spaces for spaces in result]
            if s[index] in node.right:
                result += self.dfs(s, index + 1, node.right[s[index]], trie)
            return result

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        trie = Solution.Trie()
        for w in wordDict:
            trie.put(w)
        res = self.dfs(s, 0, trie.root, trie)
        sentences = []
        for spaces in res:
            spaces.insert(0, 0)
            sentences.append(" ".join(s[spaces[i]:spaces[i + 1]] for i in range(len(spaces) - 1)))
        return sentences


class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = dict()
        for word in wordDict:
            cur = trie
            for ch in word:
                if ch not in cur:
                    cur[ch] = dict()
                cur = cur[ch]
            cur[0] = 1

        @lru_cache(None)
        def dfs(index: int) -> List[str]:
            res = []
            node = trie
            for i in range(index, len(s)):
                if s[i] not in node:
                    return res
                node = node[s[i]]
                if 0 in node:
                    res += [s[index:i + 1] + ' ' + j for j in dfs(i + 1)]
            if 0 in node:
                res.append(s[index:])
            return res

        return dfs(0)


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))
