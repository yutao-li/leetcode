from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        le = len(words[0])
        res = []
        leng = le * len(words)
        words = Counter(words)
        for i in range(len(s) - leng + 1):
            w = dict(words)
            j = i
            while j < i + leng:
                if s[j:j + le] in w:
                    w[s[j:j + le]] -= 1
                    if w[s[j:j + le]] == 0:
                        w.pop(s[j:j + le])
                    j += le
                else:
                    break
            if j == i + leng:
                res.append(i)
        return res


print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
