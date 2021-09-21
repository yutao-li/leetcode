from string import ascii_lowercase


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        ordinal = dict(zip(ascii_lowercase, range(26)))
        high = len(S)
        low = 0
        res = ''
        ha = 0
        weight = 0
        modulus = 2 ** 63 - 1
        while high > low + 1:
            mid = (high + low) // 2
            seen = set()
            dup = False
            ha1 = ha
            weight1 = weight
            for i in S[low:mid]:
                ha = (ha * 26 + ordinal[i]) % modulus
                weight = weight * 26 % modulus if weight else 1
            seen.add(ha)
            h = ha
            for i, ch in enumerate(S[mid:]):
                h = ((h - ordinal[S[i]] * weight) * 26 + ordinal[ch]) % modulus
                if h in seen:
                    low = mid
                    dup = True
                    res = S[i + 1:i + mid + 1]
                    break
                seen.add(h)
            if not dup:
                high = mid
                ha = ha1
                weight = weight1
        return res


print(Solution().longestDupSubstring(
    ''))
