from re import split


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        state = 0
        for ch in s:
            if state == 0:
                if ch == '-' or ch == '+':
                    state = 1
                elif '0' <= ch <= '9':
                    state = 2
                elif ch == '.':
                    state = 3
                else:
                    return False
            elif state == 1:
                if '0' <= ch <= '9':
                    state = 2
                elif ch == '.':
                    state = 3
                else:
                    return False
            elif state == 2:
                if '0' <= ch <= '9':
                    state = 2
                elif ch == 'e':
                    state = 6
                elif ch == '.':
                    state = 5
                else:
                    return False
            elif state == 3:
                if '0' <= ch <= '9':
                    state = 5
                else:
                    return False
            elif state == 5:
                if '0' <= ch <= '9':
                    state = 5
                elif ch == 'e':
                    state = 6
                else:
                    return False
            elif state == 6:
                if ch == '+' or ch == '-':
                    state = 7
                elif '0' <= ch <= '9':
                    state = 8
                else:
                    return False
            elif state == 7:
                if '0' <= ch <= '9':
                    state = 8
                else:
                    return False
            elif state == 8:
                if '0' <= ch <= '9':
                    state = 8
                else:
                    return False
        return state in [2, 5, 8]


class Solution1:
    def isNumber(self, s: str) -> bool:
        def isInteger(s: str):
            if not s:
                return False
            if s[0] == '+' or s[0] == '-':
                return s[1:].isdigit()
            else:
                return s.isdigit()

        def isDecimal(s: str):
            if not s:
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            parts = s.split('.')
            if len(parts) != 2:
                return False
            if parts[0]:
                if not parts[0].isdigit():
                    return False
                if parts[1] and not parts[1].isdigit():
                    return False
                return True
            else:
                return parts[1].isdigit()

        if 'e' in s or 'E' in s:
            parts = split('[eE]', s)
            if len(parts) != 2:
                return False
            return (isInteger(parts[0]) or isDecimal(parts[0])) and isInteger(parts[1])
        return isInteger(s) or isDecimal(s)


res = Solution1().isNumber("2e0")
