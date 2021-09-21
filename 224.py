class Solution:
    def calculate(self, s: str) -> int:
        operator = []
        operand = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i].isdigit():
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                if operator and operator[-1] != '(':
                    op = operator.pop()
                    if op == '+':
                        operand[-1] += int(s[i:j])
                    else:
                        operand[-1] -= int(s[i:j])
                else:
                    operand.append(int(s[i:j]))
                i = j
            elif s[i] in '+-(':
                operator.append(s[i])
                i += 1
            else:
                operator.pop()
                if operator and operator[-1] != '(':
                    j = operand.pop()
                    op = operator.pop()
                    if op == '+':
                        operand[-1] += j
                    else:
                        operand[-1] -= j
                i += 1
        while operator:
            op = operator.pop()
            n = operand.pop()
            if op == '+':
                operand[-1] += n
            else:
                operand[-1] -= n
        return operand[0]


print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
