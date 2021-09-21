from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def palin(word):
            forward = 0
            backward = 0
            pali = [0] * len(word)
            for j, ch in enumerate(word):
                forward = forward * 26 + ch
                backward += ch * power[j]
                if forward == backward:
                    pali[j] = 1
            return pali

        words = [[ord(ch) - ord('a') for ch in word] for word in words]
        power = [1]
        pa, end = -1, -2
        for _ in range(max(len(w) for w in words)):
            power.append(power[-1] * 26)
        trie = dict()
        for i, word in enumerate(words):
            tr = trie
            for ch in word[::-1]:
                if ch not in tr:
                    tr[ch] = dict()
                tr = tr[ch]
            tr[end] = i
            pal = palin(word)
            tr = trie
            for j, ch in enumerate(word[::-1]):
                if pal[-1 - j]:
                    if pa not in tr:
                        tr[pa] = []
                    tr[pa].append(i)
                tr = tr[ch]
        res = []
        for i, word in enumerate(words):
            pal = palin(word[::-1])[::-1]
            tr = trie
            for j, ch in enumerate(word):
                if pal[j] and end in tr:
                    res.append([i, tr[end]])
                if ch in tr:
                    tr = tr[ch]
                else:
                    break
            else:
                if pa in tr:
                    res += [[i, j] for j in tr[pa]]
                if end in tr and tr[end] != i:
                    res.append([i, tr[end]])
        return res


res = Solution().palindromePairs(["a", "b", "c", "ab", "ac", "aa"])
