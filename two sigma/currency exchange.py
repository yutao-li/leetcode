from functools import lru_cache


def solution(rate: [[float]], source: int, target: int) -> float:
    @lru_cache(None)
    def dfs(bit_mask, currency):
        if currency == target:
            return 1
        return max(rate[currency][i] * dfs(bit_mask | bin_rep[i], i) for i in range(n) if bin_rep[i] & bit_mask == 0)

    n = len(rate)
    bin_rep = [1 << i for i in range(n)]
    return dfs(bin_rep[source], source)
