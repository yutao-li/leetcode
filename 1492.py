class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        sqrt_n = int(n ** 0.5)
        factors = []
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                factors.append(i)
                k -= 1
                if k == 0:
                    return i
        if sqrt_n ** 2 == n:
            k += 1
        len_factors = len(factors)
        if k > len_factors:
            return -1
        else:
            return n // factors[len_factors - k]
