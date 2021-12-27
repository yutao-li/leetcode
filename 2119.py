class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return bool(num == 0 or num % 10)
