class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num1 = [int(i) for i in num1[::-1]]
        num2 = [int(i) for i in num2[::-1]]
        n1 = len(num1)
        n2 = len(num2)
        res = [0] * (n2 + 1)
        for i in range(n1):
            res[i] += num2[i] + num1[i]
            if res[i] >= 10:
                res[i + 1] = 1
                res[i] -= 10
        if n1 < n2:
            for i in range(n1, n2):
                res[i] += num2[i]
                if res[i] >= 10:
                    res[i + 1] = 1
                    res[i] -= 10
        if res[-1] == 0:
            res.pop()
        return ''.join(str(i) for i in res[::-1])
