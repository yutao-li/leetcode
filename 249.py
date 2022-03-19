from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strings:
            diff = []
            for ch1, ch2 in zip(word, word[1:]):
                d = ord(ch1) - ord(ch2)
                if d < 0:
                    d += 26
                diff.append(d)
            group[tuple(diff)].append(word)
        return list(group.values())
