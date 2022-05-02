from typing import List
from collections import defaultdict


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        changed = sorted(changed)
        original = defaultdict(int)
        double = defaultdict(int)
        for i in changed:
            if i % 2 == 0 and original[i // 2] > double[i]:
                double[i] += 1
            else:
                original[i] += 1
        if sum(original.values()) * 2 != len(changed):
            return []
        return [i for a, b in original.items() for i in [a] * b]
