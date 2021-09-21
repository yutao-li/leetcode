class Solution:
    def reformat(self, s: str) -> str:
        al = []
        di = []
        for ch in s:
            if ch.isalpha():
                al.append(ch)
            else:
                di.append(ch)
        if abs(len(al) - len(di)) > 1:
            return ''
        else:
            res = ''.join(a + b for a, b in zip(al, di))
            if len(al) > len(di):
                res += al[-1]
            elif len(di) > len(al):
                res = di[-1] + res
            return res


print(Solution().reformat('ab123'))
