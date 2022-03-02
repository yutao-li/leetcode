from functools import reduce
from itertools import combinations
from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        bin_rep = [1 << i for i in range(n)]
        has_child = [0] * n
        completion = (1 << n) - 1
        dep = [0] * n
        for i, j in dependencies:
            dep[j - 1] |= bin_rep[i - 1]
            has_child[i - 1] = 1
        seen = set()
        pool = [0]
        semester = 0
        while pool:
            pool1 = []
            for state in pool:
                can_take = [i for i in range(n) if bin_rep[i] & state == 0 and dep[i] & state == dep[i]]
                parent_take = [i for i in can_take if has_child[i]]
                leaf_take = [i for i in can_take if not has_child[i]]
                if len(parent_take) <= k:
                    to_takes = [parent_take + leaf_take[:k - len(parent_take)]]
                else:
                    to_takes = combinations(parent_take, k)
                for can_take in to_takes:
                    tmp = reduce(lambda x, y: x | y, [bin_rep[i] for i in can_take], state)
                    if tmp == completion:
                        return semester + 1
                    if tmp not in seen:
                        seen.add(tmp)
                        pool1.append(tmp)
            semester += 1
            pool = pool1


print(Solution().minNumberOfSemesters(n=4, dependencies=[[2, 1], [2, 4]], k=2))
