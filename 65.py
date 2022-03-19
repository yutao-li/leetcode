from re import split


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
