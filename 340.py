from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        window = defaultdict(int)
        left = 0
        for ch in s:
            window[ch] += 1
            if len(window) > k:
                head = s[left]
                window[head] -= 1
                if window[head] == 0:
                    del window[head]
                left += 1
        return len(s) - left


res = Solution().lengthOfLongestSubstringKDistinct('aa', 1)
