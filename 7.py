class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            neg = True
            x = -x
        else:
            neg = False
        rev = 0
        while x:
            x, r = divmod(x, 10)
            rev = 10 * rev + r
        if neg:
            rev = -rev
        if rev > 2 ** 31 - 1 or rev < -2 ** 31:
            return 0
        else:
            return rev
