class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x // 2
        while low < high:
            mid = (low + high) // 2
            if mid * mid >= x:
                high = mid
            else:
                low = mid + 1
        if low * low > x:
            low -= 1
        return low


print(Solution().mySqrt(8))
