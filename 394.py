class Solution:
    def decodeString(self, s: str) -> str:
        def helper(start):
            res = ''
            i = start
            while i < len(s) and s[i] != ']':
                if s[i].isalpha():
                    j = i
                    i += 1
                    while i < len(s) and s[i].isalpha():
                        i += 1
                    res += s[j:i]
                elif s[i].isdigit():
                    j = i
                    i += 1
                    while i < len(s) and s[i].isdigit():
                        i += 1
                    num = int(s[j:i])
                    s_res, i = helper(i + 1)
                    res += num * s_res
            return res, i + 1

        return helper(0)[0]


print(Solution().decodeString('2[abc]3[cd]ef'))
