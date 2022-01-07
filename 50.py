class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n >= 0:
            p = x
        else:
            n = -n
            p = 1 / x
        while n:
            n, r = divmod(n, 2)
            if r:
                res *= p
            p *= p
        return res
