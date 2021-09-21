class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p = [ord(c) - 97 for c in p]
        res = [0] * 26
        i = 0
        while i < len(p):
            j = i + 1
            while j < len(p) and (p[j] - p[j - 1] == 1 or p[j] - p[j - 1] == -25):
                j += 1
            k = p[i]
            leng = j - i
            while leng > j - i - 26 and leng > 0:
                if leng <= res[k % 26]:
                    break
                res[k % 26] = leng
                k += 1
                leng -= 1
            i = j
        return sum(res)


print(Solution().findSubstringInWraproundString("zaba"))
