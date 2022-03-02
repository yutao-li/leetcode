class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in match:
                stack.append(ch)
            elif not stack or match[stack.pop()] != ch:
                return False
        return not bool(stack)
