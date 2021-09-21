from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def truncate(st, brace):
            res = []
            pos = st.find(brace)
            while pos != -1:
                while pos + 1 < len(st) and st[pos + 1] == brace:
                    pos += 1
                res.append(st[:pos] + st[pos + 1:])
                pos = st.find(brace, pos + 1)
            return res

        def remove(st, brace):
            res = ['']
            i = 0
            count = 0
            start = 0
            pre = '(' if brace == ')' else ')'
            while i < len(st):
                if st[i] == pre:
                    count += 1
                elif st[i] == brace:
                    count -= 1
                    if count < 0:
                        res1 = [tr + st[start:i + 1] for prefix in res for tr in truncate(prefix, brace)]
                        res2 = [prefix + tr for prefix in res for tr in truncate(st[start:i + 1], brace)]
                        res = list(set(res1 + res2))
                        count = 0
                        start = i + 1
                i += 1
            return res, start, count

        res, start, count = remove(s, ')')
        if count > 0:
            tail = s[start:][::-1]
            res1, start1, _ = remove(tail, '(')
            res1 = [i + tail[start1:] for i in res1]
            res = [i + j[::-1] for i in res for j in res1]
        else:
            res = [i + s[start:] for i in res]
        return res


res = Solution().removeInvalidParentheses("(r(()()(")
