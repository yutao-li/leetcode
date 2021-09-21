from math import sqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))


res = Solution().bulbSwitch(3)
