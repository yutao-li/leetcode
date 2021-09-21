from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        bit = [0] * (len(queries) + 1) + [1] * m
        power = 2
        pos_map = dict((i, len(queries) + i) for i in range(1, m + 1))
        while power < len(bit):
            i = (len(queries) + 1) // power * power
            while i < len(bit):
                bit[i] += bit[i - power // 2]
                i += power
            power *= 2
        res = []
        for i, q in enumerate(queries):
            pos = pos_map[q]
            prefix = 0
            while pos:
                prefix += bit[pos]
                pos -= (pos & -pos)
            res.append(prefix - 1)
            pos = pos_map[q]
            while pos < len(bit):
                bit[pos] -= 1
                pos += (pos & -pos)
            pos = len(queries) - i
            while pos < len(bit):
                bit[pos] += 1
                pos += (pos & -pos)
            pos_map[q] = len(queries) - i
        return res


print(Solution().processQueries([4, 1, 2, 2], 4))
