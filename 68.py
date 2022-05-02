from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur = []
        leng = 0
        for w in words:
            if leng + len(cur) + len(w) <= maxWidth:
                cur.append(w)
                leng += len(w)
            else:
                if len(cur) > 1:
                    q, r = divmod(maxWidth - leng, len(cur) - 1)
                    res.append((' ' * (q + 1)).join(cur[:r + 1]) + ' ' * q + (' ' * q).join(cur[r + 1:]))
                else:
                    res.append(cur[0] + ' ' * (maxWidth - leng))
                cur = [w]
                leng = len(w)
        res.append(' '.join(cur) + ' ' * (maxWidth - leng - len(cur) + 1))
        return res


print(Solution().fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                              "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
