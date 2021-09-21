from typing import List
from collections import defaultdict


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.hot = defaultdict(int, zip(sentences, times))
        self.pos = 0
        self.history = ''
        self.candi = sentences

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.hot[self.history] += 1
            self.history = ''
            self.pos = 0
            self.candi = list(self.hot.keys())
            return []
        else:
            self.history += c
            self.candi = [i for i in self.candi if self.pos < len(i) and i[self.pos] == c]
            self.pos += 1
            return sorted(self.candi, key=lambda x: (-self.hot[x], x))[:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
