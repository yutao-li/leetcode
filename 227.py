class Solution:
    def calculate(self, s: str) -> int:
        def operate(op, a, b):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else:
                return int(a / b)

        i = 0
        s = "".join(i for i in s if i != ' ')
        res = 0
        num1 = 0
        num2 = 0
        operator = '+'
        while i < len(s):
            if s[i].isdigit():
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                num2 = int(s[i:j])
                i = j
            elif s[i] in '+-':
                num1 = operate(operator, num1, num2)
                operator = s[i]
                i += 1
            else:
                if operator in '+-':
                    res += num1
                    num1 = -num2 if operator == '-' else num2
                else:
                    num1 = operate(operator, num1, num2)
                operator = s[i]
                i += 1
        return res + operate(operator, num1, num2)


print(Solution().calculate(" 3/2 "))
