class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        symbols = [('I', 'V'), ('X', 'L'), ('C', 'D'), ('M', '')]
        i = 0
        while num and i < 3:
            num, digit = divmod(num, 10)
            if digit < 4:
                res = symbols[i][0] * digit + res
            elif digit == 4:
                res = symbols[i][0] + symbols[i][1] + res
            elif digit < 9:
                res = symbols[i][1] + symbols[i][0] * (digit - 5) + res
            elif digit == 9:
                res = symbols[i][0] + symbols[i + 1][0] + res
            i += 1
        if num == 0:
            return res
        else:
            return num * 'M' + res
