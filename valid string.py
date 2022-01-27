# https://leetcode.com/discuss/interview-question/1557009/amazon-oa-valid-string

class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if not stack or stack[-1] != ch:
                stack.append(ch)
            else:
                stack.pop()
        return bool(stack)
