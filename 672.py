class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if n > 2:
            return 8 if m >= 3 else [1, 4, 7][m]
        elif n == 2:
            return 4 if m >= 2 else [1, 3][m]
        elif n == 1:
            return 1 if m == 0 else 2
        else:
            return 0
