from functools import reduce
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        stack = []
        res = max(nums)
        for n in nums + [0]:
            if n == 0:
                if stack:
                    negs = [i for i, j in enumerate(stack) if j < 0]
                    if len(negs) % 2 == 0:
                        res = max(res, reduce(lambda x, y: x * y, stack))
                    else:
                        if negs[-1] > 0:
                            res = max(res, reduce(lambda x, y: x * y, stack[:negs[-1]]))
                        if negs[0] < len(stack) - 1:
                            res = max(res, reduce(lambda x, y: x * y, stack[negs[0] + 1:]))
                stack = []
            elif n > 0 and stack and stack[-1] > 0:
                stack[-1] *= n
            else:
                stack.append(n)
        return res


print(Solution().maxProduct(nums=[2, -5, -2, -4, 3]))
