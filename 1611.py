# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/877809/GreyCode-to-decimal-C%2B%2B-Math-solution

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = n
        n >>= 1
        while n:
            res ^= n
            n >>= 1
        return res


# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/878086/O(1)-Solution

class Solution1:
    def minimumOneBitOperations(self, n: int) -> int:
        n = n ^ n >> 16
        n = n ^ n >> 8
        n = n ^ n >> 4
        n = n ^ n >> 2
        n = n ^ n >> 1
        return n
