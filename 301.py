class Solution:
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0

        level = {s}
        while True:
            valid = list(filter(isvalid, level))
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}


class Solution1:
    def removeInvalidParentheses(self, s) -> [str]:
        def remove(cur_s: str, cur_i: int, last_remove: int, braces: [str, str]):
            balance = 0
            for i in range(cur_i, len(cur_s)):
                if cur_s[i] == braces[0]:
                    balance += 1
                elif cur_s[i] == braces[1]:
                    balance -= 1
                if balance < 0:
                    for j in range(last_remove, i + 1):
                        if cur_s[j] == braces[1] and (j == last_remove or cur_s[j - 1] != braces[1]):
                            remove(cur_s[:j] + cur_s[j + 1:], i, j, braces)
                    return
            if balance == 0:
                if braces[0] == '(':
                    res.append(cur_s)
                else:
                    res.append(cur_s[::-1])
            else:
                remove(cur_s[::-1], 0, 0, braces[::-1])

        res = []
        remove(s, 0, 0, ['(', ')'])
        return res


res = Solution1().removeInvalidParentheses("(r(()()(")
print(res)
