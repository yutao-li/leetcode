class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s1) >= set(s2):
            return 0
        s1 = ''.join(ch for ch in s1 if ch in set(s2))
        i2 = 0
        start = [0] * len(s2)
        start[0] = (0, 0)
        count_round = [0] * (n1 + 1)
        for round in range(1, n1 + 1):
            for ch in s1:
                if s2[i2 % len(s2)] == ch:
                    i2 += 1
            c, i = divmod(i2, len(s2))
            if not start[i]:
                start[i] = (round, c)
                count_round[round] = c
            else:
                pre_round, pre_c = start[i]
                q, r = divmod(n1 - pre_round, round - pre_round)
                return ((c - pre_c) * q + count_round[pre_round + r]) // n2
        return i2 // (len(s2) * n2)


res = Solution().getMaxRepetitions("bacaba", 3, "abacab", 1)
