class Solution:
    def calculate(self, s: str) -> int:
        def operate(op, b, a):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else:
                return a // b

        operator = []
        operand = []
        i = 0
        s = "".join(i for i in s if i != ' ')
        while i < len(s):
            if s[i].isdigit():
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                operand.append(int(s[i:j]))
                i = j
            elif s[i] in '+-':
                while operator:
                    operand.append(operate(operator.pop(), operand.pop(), operand.pop()))
                operator.append(s[i])
                i += 1
            else:
                while operator and operator[-1] in '*/':
                    operand.append(operate(operator.pop(), operand.pop(), operand.pop()))
                operator.append(s[i])
                i += 1
        while operator:
            operand.append(operate(operator.pop(), operand.pop(), operand.pop()))
        return operand[0]


print(Solution().calculate(" 3/2 "))
