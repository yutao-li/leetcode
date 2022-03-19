from functools import lru_cache
from typing import List


class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def dfs(index: int) -> List[str]:
            res = []
            node = trie
            for i in range(index, len(s)):
                if s[i] not in node:
                    return res
                node = node[s[i]]
                if 0 in node:
                    res += [node[0] + ' ' + j for j in dfs(i + 1)]
            if 0 in node:
                res.append(node[0])
            return res

        trie = dict()
        for word in wordDict:
            cur = trie
            for ch in word:
                if ch not in cur:
                    cur[ch] = dict()
                cur = cur[ch]
            cur[0] = word
        return dfs(0)


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution1().wordBreak(s, wordDict))
