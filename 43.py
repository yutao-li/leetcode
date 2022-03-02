class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mul(num, di):
            acc = 0
            di = int(di)
            for i in num:
                acc = 10 * acc + di * int(i)
            return acc

        acc = 0
        for i in num2:
            acc = 10 * acc + mul(num1, i)
        return str(acc)
