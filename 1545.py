class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        inv = False
        le = 0
        for _ in range(n):
            le = 2 * le + 1
        k -= 1
        while le != 1:
            d = k - le // 2
            if d == 0:
                return str(int(not inv))
            elif d < 0:
                le //= 2
            else:
                k -= le // 2
                k = le // 2 - k
                le //= 2
                inv = not inv
        return str(int(inv))


res = Solution().findKthBit(n=4, k=12)

