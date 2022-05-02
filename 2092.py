from typing import List
from collections import defaultdict


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return
            if height[a] > height[b]:
                parent[b] = a
            elif height[a] < height[b]:
                parent[a] = b
            else:
                parent[b] = a
                height[a] += 1

        ts2meetings = defaultdict(list)
        height = [0] * n
        parent = list(range(n))
        union(0, firstPerson)
        for x, y, ts in meetings:
            ts2meetings[ts].append([x, y])
        for i in sorted(ts2meetings):
            involved = set()
            for x, y in ts2meetings[i]:
                union(x, y)
                involved.add(x)
                involved.add(y)
            for person in involved:
                if find(0) != find(person):
                    parent[person] = person
                    height[person] = 0
        return [i for i in range(n) if find(i) == find(0)]


print(Solution().findAllPeople(11, [[5, 1, 4], [0, 4, 18]], 1))
