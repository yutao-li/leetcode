from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words.sort(key=len)
        pos = dict((len(w), i) for i, w in enumerate(words))
        for word in words:
            for w in words[pos[len(word)] + 1:]:
                if word in w:
                    res.append(word)
                    break
        return res
