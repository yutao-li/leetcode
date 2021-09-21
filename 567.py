from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        c1 = Counter(s1)
        c2 = Counter(s2[:n1])
        for k, v in c1.items():
            c2[k] -= v
        zero = sum(v == 0 for v in c2.values())
        n3 = len(c2)
        if zero == n3:
            return True
        i = n1
        while i < n2:
            c2[s2[i]] += 1
            v = c2[s2[i]]
            if v == 0:
                zero += 1
            elif v == 1:
                zero -= 1
            c2[s2[i - n1]] -= 1
            v = c2[s2[i - n1]]
            if v == 0:
                zero += 1
            elif v == -1:
                zero -= 1
            if zero == n3:
                return True
            i += 1
        return False


res = Solution().checkInclusion(s1= "ab", s2 = "eidboaoo")
