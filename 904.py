from typing import List
from collections import defaultdict


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ty = defaultdict(int)
        left = right = 0
        ty[tree[0]] = 1
        width = 1
        while right + 1 < len(tree):
            if len(ty) == 1 or tree[right + 1] in ty:
                ty[tree[right + 1]] += 1
                right += 1
            else:
                width = max(width, right - left + 1)
                while len(ty) == 2:
                    ty[tree[left]] -= 1
                    if ty[tree[left]] == 0:
                        del ty[tree[left]]
                    left += 1
        width = max(width, right - left + 1)
        return width


print(Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
