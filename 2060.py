from functools import cache


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        @cache
        def getLengths(s: str) -> {int}:
            res = {x + y for i in range(1, len(s)) for x in getLengths(s[:i]) for y in getLengths(s[i:])}
            res.add(int(s))
            return res

        @cache
        def dfs(s1: str, s2: str, diff: int) -> bool:
            if not s1 and not s2:
                return diff == 0
            if s1 and s1[0].isdigit():
                j = 1
                while j < len(s1) and s1[j].isdigit():
                    j += 1
                ls = getLengths(s1[:j])
                for l in ls:
                    if dfs(s1[j:], s2, diff - l):
                        return True
            elif s2 and s2[0].isdigit():
                return dfs(s2, s1, -diff)
            elif diff > 0 and s1:
                return dfs(s1[1:], s2, diff - 1)
            elif diff < 0 and s2:
                return dfs(s2, s1, -diff)
            else:
                return s1 and s2 and s1[0] == s2[0] and dfs(s1[1:], s2[1:], 0)
            return False

        return dfs(s1, s2, 0)


print(Solution().possiblyEquals("l123e", "44"))
