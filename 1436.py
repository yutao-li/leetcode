from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = set()
        start = set()
        for a, b in paths:
            dest.add(b)
            start.add(a)
        return list(dest - start)[0]


res = Solution().destCity([["A","Z"]])
