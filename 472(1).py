from typing import List
from functools import lru_cache


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        @lru_cache(None)
        def dfs(word):
            if word in pre:
                return True
            for i in pre_len[1:]:
                if len(word[i:]) < pre_len[1]:
                    break
                if word[:i] in pre and (word[i:] in pre or dfs(word[i:])):
                    return True
            return False

        if not words:
            return []
        words.sort(key=len)
        pre = set()
        pre_len = [0]
        res = []
        for w in words:
            if dfs(w):
                res.append(w)
            pre.add(w)
            if len(w) > pre_len[-1]:
                pre_len.append(len(w))
        return res


res = Solution().findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"])
