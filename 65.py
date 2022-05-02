from re import split


class Solution:
    def isNumber(self, s: str) -> bool:
        def isInteger(s: str):
            if not s:
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            return s.isdigit()

        def isDecimal(s: str):
            if not s:
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            parts = s.split('.')
            if len(parts) != 2:
                return False
            if not (parts[0] or parts[1]):
                return False
            return all(not i or i.isdigit() for i in parts)

        if 'e' in s or 'E' in s:
            parts = split('[eE]', s)
            if len(parts) != 2:
                return False
            return (isInteger(parts[0]) or isDecimal(parts[0])) and isInteger(parts[1])
        return isInteger(s) or isDecimal(s)


res = Solution().isNumber("2e0")
