class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def calculate(num):
            num_eq = str(num).count(str(d))
            res = 0
            acc0 = 0
            acc1 = 1
            while num:
                num, di = divmod(num, 10)
                num_eq -= di == d
                res += di * num_eq * acc1 + di * acc0
                # to remove count of numbers with leading 0s
                if d == 0:
                    res -= acc1
                if di > d:
                    res += acc1
                acc0 = 10 * acc0 + acc1
                acc1 *= 10
            return res

        return calculate(high + 1) - calculate(low)


print(Solution().digitsCount(0, 625, 1250))
