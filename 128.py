from typing import List
from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(p):
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        longest = 0
        parent = dict()
        size = dict()
        rank = defaultdict(int)
        for num in set(nums):
            if num - 1 in parent and num + 1 in parent:
                rootP = find(num - 1)
                rootQ = find(num + 1)
                if rank[rootP] > rank[rootQ]:
                    rootP, rootQ = rootQ, rootP
                elif rank[rootP] == rank[rootQ]:
                    rank[rootQ] += 1
                parent[rootP] = rootQ
                size[rootQ] += size[rootP] + 1
            elif num - 1 in parent:
                rootQ = find(num - 1)
                size[rootQ] += 1
            elif num + 1 in parent:
                rootQ = find(num + 1)
                size[rootQ] += 1
            else:
                rootQ = num
                size[num] = 1
            parent[num] = rootQ
            if rootQ != num and rank[rootQ] == 0:
                rank[rootQ] += 1
            longest = max(longest, size[rootQ])
        return longest


res = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
