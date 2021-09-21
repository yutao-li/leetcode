class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a0, a1 = 1, 2
        for _ in range(n - 2):
            a2 = a1 + a0
            a1, a0 = a2, a1
        return a1
