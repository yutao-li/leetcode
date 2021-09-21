class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        return self.dp(len(s3) - 1, len(s1) - 1, len(s2) - 1, s1, s2, s3, {})

    def dp(self, e3, e1, e2, s1, s2, s3, mem):
        if (e3, e1, e2) in mem:
            return mem[e3, e1, e2]
        if e1 == -1:
            res = s3[:e3 + 1] == s2[:e2 + 1]
        elif e2 == -1:
            res = s3[:e3 + 1] == s1[:e1 + 1]
        else:
            if s1[e1] != s2[e2]:
                if s3[e3] == s1[e1]:
                    res = self.dp(e3 - 1, e1 - 1, e2, s1, s2, s3, mem)
                elif s3[e3] == s2[e2]:
                    res = self.dp(e3 - 1, e1, e2 - 1, s1, s2, s3, mem)
                else:
                    res = False
            else:
                if s3[e3] != s1[e1]:
                    res = False
                else:
                    res = self.dp(e3 - 1, e1 - 1, e2, s1, s2, s3, mem) or self.dp(e3 - 1, e1, e2 - 1, s1, s2, s3, mem)
        mem[e3, e1, e2] = res
        return res


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(Solution().isInterleave(s1, s2, s3))
