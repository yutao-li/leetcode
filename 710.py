from random import randrange
from typing import List


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        blacklist = [i for i in blacklist if i < n]
        m = len(blacklist)
        included = [i for i in blacklist if i < n - m]
        excluded = set(i for i in blacklist if i >= n - m)
        values = [i for i in range(n - m, n) if i not in excluded]
        self.holes = dict(zip(included, values))
        self.n = n - m

    def pick(self) -> int:
        r = randrange(self.n)
        return self.holes.get(r, r)

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
