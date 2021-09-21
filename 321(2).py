from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        next_pos1 = self.get_next_pos(nums1)
        next_pos2 = self.get_next_pos(nums2)

        solution = [None] * k

        candidates = [(0, 0)]
        for l in range(k):
            candidates = self.prune_candidates(candidates)
            num = self.select_num(candidates, next_pos1, next_pos2, m, n, k - l)
            solution[l] = num
            if l == k - 1:
                break
            next_candidates = []
            for i, j in candidates:
                if next_pos1[i][num] is not None and m - next_pos1[i][num] + n - j >= k - l:
                    next_candidates.append((next_pos1[i][num] + 1, j))
                if next_pos2[j][num] is not None and m - i + n - next_pos2[j][num] >= k - l:
                    next_candidates.append((i, next_pos2[j][num] + 1))
            candidates = next_candidates

        return solution

    def get_next_pos(self, nums):
        m = len(nums)
        next_pos = [None] * (m + 1)
        next_pos[m] = [None] * 10
        for i in reversed(range(m)):
            next_pos[i] = next_pos[i + 1].copy()
            next_pos[i][nums[i]] = i
        return next_pos

    def select_num(self, candidates, next_pos1, next_pos2, m, n, remaining):
        for num in reversed(range(10)):
            for i, j in candidates:
                if next_pos1[i][num] is not None and m - next_pos1[i][num] + n - j >= remaining:
                    break
                if next_pos2[j][num] is not None and m - i + n - next_pos2[j][num] >= remaining:
                    break
            else:
                continue
            return num

    def prune_candidates(self, candidates):
        i_min_j = {}
        j_min_i = {}
        pruned_candidates = []
        for i, j in candidates:
            if i in i_min_j and i_min_j[i] <= j:
                continue
            if j in j_min_i and j_min_i[j] <= i:
                continue
            pruned_candidates.append((i, j))
            i_min_j[i] = j
            j_min_i[j] = i
        return pruned_candidates


print(Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
