# https://leetcode.com/discuss/interview-question/1527679/amazon-oa-password-strength
from collections import defaultdict


class Solution:
    def password_strength(self, s: str) -> int:
        pos = defaultdict(list)
        n = len(s)
        for i, ch in enumerate(s):
            pos[ch].append(i)
        return sum(sum((j - i) * (n - j) for i, j in zip([-1] + v, v)) for v in pos.values())


print(Solution().password_strength("abc"))
