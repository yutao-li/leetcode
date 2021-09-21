class Solution:
    def numOfWays(self, n: int) -> int:
        if n == 1:
            return 12
        modulo = int(1e9 + 7)
        a = b = 1
        for _ in range(n - 2):
            a, b = (3 * a + 2 * b) % modulo, 2 * (a + b) % modulo
        return (30 * a + 24 * b) % modulo


print(Solution().numOfWays(3))
