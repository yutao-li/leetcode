"""
This is Master's API interface.
You should not implement it, or speculate about its implementation
"""


class Master:
    def guess(self, word: str) -> int:
        pass


from typing import List


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        num = dict(zip(wordlist, range(len(wordlist))))
        overlap = [[6] * len(wordlist) for _ in range(len(wordlist))]
        for i, w1 in enumerate(wordlist):
            for j, w2 in enumerate(wordlist[i + 1:], start=i + 1):
                overlap[i][j] = sum(a == b for a, b in zip(w1, w2))
                overlap[j][i] = overlap[i][j]
        while True:
            word = ''
            size = 0
            for w in wordlist:
                size1 = sum(1 for w1 in wordlist if overlap[num[w]][num[w1]])
                size1 = max(size1, len(wordlist) - size1)
                if not word or size > size1:
                    word = w
                    size = size1
            match = master.guess(word)
            if match == 6:
                return
            wordlist = [w for w in wordlist if overlap[num[w]][num[word]] == match]
