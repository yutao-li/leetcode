class Solution:
    def lastSubstring(self, s: str) -> str:
        prefix = max(s)
        le = len(s)
        pool = [i for i, ch in enumerate(s) if ch == prefix and (i == 0 or s[i - 1] != prefix)]
        while len(pool) > 1:
            ch = max(s[i + 1] for i in pool if i + 1 < le)
            prefix += ch
            pool = [i + 1 for i in pool if i + 1 < le and s[i + 1] == ch]
        return prefix if not pool else prefix + s[pool[0] + 1:]


res = Solution().lastSubstring("abab")
