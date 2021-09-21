from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if len(arr) < m * k:
            return False
        count = 0
        for i, n in enumerate(arr[:len(arr) - m]):
            if arr[i + m] != n:
                count = 0
            else:
                count += 1
            if count == (k - 1) * m:
                return True
        return False


res = Solution().containsPattern([1, 2, 1, 2, 1, 3], 2, 3)
