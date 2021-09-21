class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for ch in S:
            if ch == '(':
                stack.append(ch)
            else:
                if stack[-1] == '(':
                    stack[-1] = 1
                else:
                    v = stack.pop()
                    stack.pop()
                    stack.append(2 * v)
                if len(stack) >= 2 and type(stack[-2]) is int:
                    a = stack.pop()
                    stack[-1] += a
        return stack[0]


print(Solution().scoreOfParentheses('(()(()))'))
