from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dfs(s: str):
            for word in wordDict:
                if s == word or s.startswith(word) and dfs(s[len(word):]):
                    return True
            return False

        wordDict.sort(key=len, reverse=True)
        return dfs(s)


res = Solution().wordBreak('leetcode', ["leet", "code"])
