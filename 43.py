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


class Solution1:
    def multiply(self, num1: str, num2: str) -> str:
        if num2 == '0' or num1 == '0':
            return '0'
        N = len(num1) + len(num2)
        res = [0] * N
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i, d1 in enumerate(num1):
            for j, d2 in enumerate(num2):
                pos = i + j
                carry = res[pos]
                q, r = divmod(int(d1) * int(d2) + carry, 10)
                res[pos] = r
                res[pos + 1] += q
        if res[-1] == 0:
            res.pop()
        return ''.join(str(i) for i in res[::-1])
