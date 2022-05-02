from typing import List
from functools import cache
from itertools import chain


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def possibleResults(begin: int, end: int) -> [int]:
            if begin == end:
                return [expression[begin]]
            res = []
            for i in range(begin + 1, end, 2):
                left = possibleResults(begin, i - 1)
                right = possibleResults(i + 1, end)
                if expression[i] == '+':
                    res1 = [a + b for a in left for b in right]
                elif expression[i] == '-':
                    res1 = [a - b for a in left for b in right]
                else:
                    res1 = [a * b for a in left for b in right]
                res += res1
            return res

        n = len(expression)
        operators = [i for i, ch in enumerate(expression) if not ch.isdigit()]
        operands = [int(expression[i + 1:j]) for i, j in zip([-1] + operators, operators + [n])]
        operators = [expression[i] for i in operators]
        expression = list(chain(*zip(operands, operators))) + [operands[-1]]
        n = len(expression)
        return possibleResults(0, n - 1)


print(Solution().diffWaysToCompute(expression="2*3-4*5"))
