from collections import defaultdict
from bisect import bisect


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5:
            return -1
        pos = defaultdict(list)
        for i, ch in enumerate(croakOfFrogs):
            pos[ch].append(i)
        if not (len(pos['c']) == len(pos['r']) == len(pos['o']) == len(pos['a']) == len(pos['k'])):
            return -1
        for i in range(len(croakOfFrogs) // 5):
            if not (pos['c'][i] < pos['r'][i] < pos['o'][i] < pos['a'][i] < pos['k'][i]):
                return -1
        res = 1
        for i in range(len(croakOfFrogs) // 5):
            res = max(res, bisect(pos['c'], pos['k'][i], i) - i)
        return res


print(Solution().minNumberOfFrogs('croakcroa'))
