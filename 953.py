from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = dict(zip(order, range(len(order))))
        for w1, w2 in zip(words, words[1:]):
            lt = False
            for ch1, ch2 in zip(w1, w2):
                if pos[ch1] > pos[ch2]:
                    return False
                if pos[ch1] < pos[ch2]:
                    lt = True
                    break
            if not lt and len(w1) > len(w2):
                return False
        return True


res = Solution().isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")

