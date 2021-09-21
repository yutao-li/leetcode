class Solution:
    def countDigitOne(self, n: int) -> int:
        n += 1
        num_eq = str(n).count('1')
        res = 0
        acc0 = 0
        acc1 = 1
        while n:
            n, di = divmod(n, 10)
            num_eq -= di == 1
            res += di * num_eq * acc1 + di * acc0
            if di > 1:
                res += acc1
            acc0 = 10 * acc0 + acc1
            acc1 *= 10
        return res

print(Solution().countDigitOne(13))
