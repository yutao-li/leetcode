from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        le = len(words[0])
        res = []
        leng = le * len(words)
        words = Counter(words)
        for i in range(le):
            start = i
            j = start + leng
            w = Counter(words)
            while j - 1 < len(s):
                while j > start:
                    word = s[j - le:j]
                    if w[word] > 0:
                        w[word] -= 1
                        j -= le
                    else:
                        start = j
                        j = start + leng
                        w = Counter(words)
                        break
                if j == start:
                    res.append(start)
                    while s[start:start + le] == s[start + leng:start + leng + le]:
                        res.append(start + le)
                        start += le
                    start += le
                    j = start + leng
                    w = Counter(words)
        return res


print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
