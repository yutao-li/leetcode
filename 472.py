from typing import List
from functools import lru_cache


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = dict()
        for w in words:
            tr = trie
            for ch in w:
                if ch not in tr:
                    tr[ch] = {}
                tr = tr[ch]
            tr[0] = 0

        @lru_cache(None)
        def dfs(word, init):
            tr = trie
            for i, ch in enumerate(word[:-1]):
                if ch not in tr:
                    return False
                tr = tr[ch]
                if 0 in tr and dfs(word[i + 1:], False):
                    return True
            return not init and word[-1] in tr and 0 in tr[word[-1]]

        words.sort(key=len)
        res = []
        for w in words:
            if dfs(w, True):
                res.append(w)
        return res


res = Solution().findAllConcatenatedWordsInADict(
    ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"])
