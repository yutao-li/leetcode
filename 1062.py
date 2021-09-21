class Solution:
    def longestRepeatingSubstring(self, S: str) -> str:
        high = len(S)
        low = 0
        while high > low + 1:
            mid = (high + low) // 2
            seen = set()
            dup = False
            for i in range(len(S) - mid + 1):
                h = hash(S[i:i + mid])
                if h in seen:
                    low = mid
                    dup = True
                    break
                seen.add(h)
            if not dup:
                high = mid
        return low


print(Solution().longestRepeatingSubstring('aaaaa'))
