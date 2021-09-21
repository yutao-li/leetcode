from typing import *


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = dict()
        self.di = dict(zip(words, range(len(words))))
        self.trie[0] = len(words) - 1
        for weight, word in enumerate(words):
            tmp = self.trie
            i = 0
            j = len(word) - 1
            while i < j:
                i1, j1, tmp1 = i, j, tmp
                while i1 <= j1:
                    pair = word[i1], None
                    if pair not in tmp1:
                        tmp1[pair] = dict()
                    tmp1 = tmp1[pair]
                    tmp1[0] = weight
                    i1 += 1

                i1, j1, tmp1 = i, j, tmp
                while i1 <= j1:
                    pair = None, word[j1]
                    if pair not in tmp1:
                        tmp1[pair] = dict()
                    tmp1 = tmp1[pair]
                    tmp1[0] = weight
                    j1 -= 1

                pair = word[i], word[j]
                if pair not in tmp:
                    tmp[pair] = dict()
                tmp = tmp[pair]
                i += 1
                j -= 1
                tmp[0] = weight
            if len(word) % 2 != 0:
                mid = word[len(word) // 2]
                tmp1 = tmp
                if (mid, None) not in tmp1:
                    tmp1[mid, None] = dict()
                tmp1 = tmp1[mid, None]
                tmp1[0] = weight

                tmp1 = tmp
                if (None, mid) not in tmp1:
                    tmp1[None, mid] = dict()
                tmp1 = tmp1[None, mid]
                tmp1[0] = weight

    def f(self, prefix: str, suffix: str) -> int:
        weight = -1
        overlap = min(len(prefix), len(suffix))
        for i in range(1, overlap + 1):
            if prefix[-i:] == suffix[:i]:
                word = prefix + suffix[i:]
                if word in self.di:
                    weight = max(weight, self.di[word])

        i = 0
        length = max(len(prefix), len(suffix))
        suffix = suffix[::-1]
        if len(prefix) < length:
            prefix = list(prefix) + [None] * (length - len(prefix))
        else:
            suffix = list(suffix) + [None] * (length - len(suffix))
        cur = self.trie
        while i < length:
            word = prefix[i], suffix[i]
            if word not in cur:
                return weight
            cur = cur[word]
            i += 1
        # weight = -1
        # while cur:
        #     weight = max(weight, max((di[0] for di in cur if 0 in di), default=-1))
        #     cur = [v for di in cur for k, v in di.items() if k != 0]
        return cur[0]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
x = WordFilter(["pop"])
res = x.f("p", "p")
res1 = x.f("b", "")
