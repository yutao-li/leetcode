from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = [[] for _ in range(n)]
        for i, j in enumerate(manager):
            if i != headID:
                subs[j].append(i)
        pool = [headID]
        while pool:
            for i in pool:
                for subor in subs[i]:
                    informTime[subor] += informTime[i]
            pool = [subor for i in pool for subor in subs[i]]
        return max((t for i, t in enumerate(informTime) if subs[i]), default=0)


res = Solution().numOfMinutes(n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914])

