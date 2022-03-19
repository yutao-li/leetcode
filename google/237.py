from functools import lru_cache


def FindFirstCharOutOfAlphaOrder(s):
    @lru_cache(None)
    def maxLength(ch: str, i: int):
        if i == n:
            return 0
        if ch > s[i]:
            return maxLength(ch, i + 1)
        else:
            return max(1 + maxLength(s[i], i + 1), maxLength(ch, i + 1))

    n = len(s)
    return n - maxLength('', 0)


print(FindFirstCharOutOfAlphaOrder('BEEXHIVE'))
