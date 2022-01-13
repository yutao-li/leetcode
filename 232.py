from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(left, right, op1, op2, op3):
            op = op1 + op2 * op3
            if not right:
                if op == target:
                    res.append(left)
                return
            r = int(right[0])
            dfs(left + '+' + right[0], right[1:], op, 1, r)
            dfs(left + '-' + right[0], right[1:], op, -1, r)
            dfs(left + '*' + right[0], right[1:], op1, op2 * op3, r)
            if op3:
                dfs(left + right[0], right[1:], op1, op2, op3 * 10 + r)

        res = []
        dfs(num[0], num[1:], 0, 1, int(num[0]))  # exp can always be truncated to op1+op2*op3
        return res


mine = sorted(Solution().addOperators("123456789", 45))
