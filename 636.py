from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        pre_ts = 0
        id_stack = [0]
        for log in logs[1:]:
            id, action, ts = log.split(':')
            id, ts = int(id), int(ts)
            if action == 'start':
                if id_stack:
                    res[id_stack[-1]] += ts - pre_ts
                id_stack.append(id)
                pre_ts = ts
            else:
                res[id_stack.pop()] += ts - pre_ts + 1
                pre_ts = ts + 1
        return res


print(Solution().exclusiveTime(2, ["0:start:0", "0:start:2", "0:end:5", "1:start:7", "1:end:7", "0:end:8"]))
