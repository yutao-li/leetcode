from typing import List
from collections import defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def dfs(ch):
            visited[ch] = 0
            for ch1 in rev_adj[ch]:
                if ch1 in visited:
                    if visited[ch1] == 0:
                        return True
                elif dfs(ch1):
                    return True
            order.append(ch)
            visited[ch] = 1
            return False

        rev_adj = defaultdict(list)
        alphabet = set()
        for w in words:
            alphabet |= set(w)
        for w1, w2 in zip(words, words[1:]):
            for ch1, ch2 in zip(w1, w2):
                if ch1 != ch2:
                    rev_adj[ch2].append(ch1)
                    break
            else:
                if len(w1) > len(w2):
                    return ''
        visited = dict()
        order = []
        for ch in alphabet:
            if ch not in visited and dfs(ch):
                return ''
        return ''.join(order)


res = Solution().alienOrder(["abc", "ab"])
