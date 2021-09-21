from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(w):
            return ''.join('*' if ch in 'aeiou' else ch for ch in w)

        m1 = dict()
        m2 = dict()
        for w in wordlist:
            m1.setdefault(w.lower(), w)
            m2.setdefault(devowel(w.lower()), w)
        wordlist = set(wordlist)
        return [q if q in wordlist else m1.get(q.lower(), m2.get(q.lower(), '')) for q in queries]


res = Solution().spellchecker(wordlist=["KiTe", "kite", "hare", "Hare"],
                              queries=["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"])
