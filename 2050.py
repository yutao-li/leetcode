from collections import defaultdict
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        dep = defaultdict(list)
        rev_dep = defaultdict(list)
        in_deg = [0] * n
        for i, j in relations:
            dep[i - 1].append(j - 1)
            rev_dep[j - 1].append(i - 1)
            in_deg[j - 1] += 1
        completion = [0] * n
        pool = [i for i in range(n) if in_deg[i] == 0]
        while pool:
            pool1 = []
            for i in pool:
                completion[i] = time[i] + max((completion[j] for j in rev_dep[i]), default=0)
                for j in dep[i]:
                    in_deg[j] -= 1
                    if in_deg[j] == 0:
                        pool1.append(j)
            pool = pool1
        return max(completion)


print(Solution().minimumTime(n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]))
