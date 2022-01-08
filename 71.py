class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = [i for i in path.split('/') if i and i != '.']
        stack = []
        for p in parts:
            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)
