class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        close_count = 0
        open_count = 0
        for ch in s:
            if ch == '(':
                open_count += 1
            elif ch == ')':
                if open_count:
                    open_count -= 1
                else:
                    close_count += 1
        return open_count + close_count
