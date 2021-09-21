from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur = []
        le = 0
        for w in words:
            if le + len(cur) + len(w) <= maxWidth:
                cur.append(w)
                le += len(w)
            else:
                if len(cur) == 1:
                    res.append(cur[0] + ' ' * (maxWidth - le))
                else:
                    quotient, remainder = divmod(maxWidth - le, len(cur) - 1)
                    line = ''
                    for i, w1 in enumerate(cur[:-1]):
                        line += w1 + ' ' * quotient
                        if i < remainder:
                            line += ' '
                    line += cur[-1]
                    res.append(line)
                cur = [w]
                le = len(w)
        if cur:
            res.append(' '.join(cur) + ' ' * (maxWidth - le - len(cur) + 1))
        return res


print(Solution().fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                              "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
