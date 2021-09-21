class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        rep = 0
        count_r = [0, 0, 0]
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                q, r = divmod(j - i, 3)
                rep += q
                count_r[r] += 1
            i = j
        no_di = not any(ch.isdigit() for ch in s)
        no_lo = not any(ch.islower() for ch in s)
        no_up = not any(ch.isupper() for ch in s)
        missing = no_di + no_lo + no_up
        if len(s) < 6:
            return max(6 - len(s), missing)
        elif 6 <= len(s) <= 20:
            return max(missing, rep)
        else:
            dele = len(s) - 20
            if dele > count_r[0]:
                rep -= count_r[0]
                dele -= count_r[0]
                if dele > 2 * count_r[1]:
                    rep -= count_r[1]
                    dele -= 2 * count_r[1]
                    rep -= dele // 3
                else:
                    rep -= dele // 2
            else:
                rep -= dele
            return len(s) - 20 + max(rep, missing)


res = Solution().strongPasswordChecker("")
