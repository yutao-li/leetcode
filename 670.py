class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(i) for i in str(num)]
        n = len(digits)
        max_i = n - 1
        swap_i, swap_j = 0, 0
        for i in range(n - 1, -1, -1):
            if digits[i] > digits[max_i]:
                max_i = i
            elif digits[i] < digits[max_i]:
                swap_i = i
                swap_j = max_i
        digits[swap_i], digits[swap_j] = digits[swap_j], digits[swap_i]
        return int(''.join(str(i) for i in digits))
