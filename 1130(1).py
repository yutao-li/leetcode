from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        res = 0
        for i in arr:
            while stack[-1] < i:
                res += stack.pop() * min(stack[-1], i)
            stack.append(i)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res


res = Solution().mctFromLeafValues([6, 2, 4])
