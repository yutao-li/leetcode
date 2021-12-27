from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = len(t)
        t = Counter(t)
        left = right = 0
        window = defaultdict(int)
        cur = 0
        while cur < c and right < len(s):
            ch = s[right]
            if ch in t:
                window[ch] += 1
                if window[ch] <= t[ch]:
                    cur += 1
            right += 1
        if cur < c:
            return ''
        res = s[:right]
        while cur == c:
            ch = s[left]
            left += 1
            if ch in t:
                window[ch] -= 1
                if window[ch] < t[ch]:
                    if len(res) > right - left + 1:
                        res = s[left - 1:right]
                    while window[ch] < t[ch] and right < len(s):
                        ch1 = s[right]
                        if ch1 in t:
                            window[ch1] += 1
                        right += 1
                    if window[ch] < t[ch]:
                        cur -= 1
        return res


s = "a"
t = "aa"
print(Solution().minWindow(s, t))
