class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        zero_from = [0] * (len(S) + 1)
        count = 0
        for i in range(len(S) - 1, -1, -1):
            if S[i] == '0':
                count += 1
            zero_from[i] = count
        one_before = [0] * (len(S) + 1)
        count = 0
        for i in range(len(S)):
            if S[i] == '1':
                count += 1
            one_before[i + 1] = count
        return min(a + b for a, b in zip(zero_from, one_before))


print(Solution().minFlipsMonoIncr('00011000'))
