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


res = Solution().isNumber("256523.e02")
