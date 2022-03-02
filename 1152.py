from collections import defaultdict
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        records = sorted(zip(timestamp, username, website))
        user_records = defaultdict(list)
        for ts, u, w in records:
            user_records[u].append(w)
        pattern_count = defaultdict(int)
        for websites in user_records.values():
            n = len(websites)
            patterns = set((websites[i], websites[j], websites[k]) for i in range(n) for j in range(i + 1, n) for k in
                           range(j + 1, n))
            for p in patterns:
                pattern_count[p] += 1
        res = []
        max_count = 0
        for pattern, count in pattern_count.items():
            if count > max_count or count == max_count and pattern < res:
                max_count = count
                res = pattern
        return res
