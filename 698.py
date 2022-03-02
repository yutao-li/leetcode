from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        nums.sort()
        summ = sum(nums)
        n = len(nums)
        target, r = divmod(summ, k)
        if r:
            return False

        subset_sum = [-1] * (1 << n)
        subset_sum[0] = 0
        for i, s in enumerate(subset_sum):
            if s == -1:
                continue
            for j, num in enumerate(nums):
                if num + s > target:
                    break
                if i & (1 << j) == 0 and s + num <= target:
                    subset_sum[i | (1 << j)] = 0 if s + num == target else s + num
                    if subset_sum[-1] == 0:
                        return True
        return False


class Solution1:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(i, acc, bit_mask, count):
            if bit_mask in false_masks:
                return False
            for j in range(i, n):
                if nums[j] + acc > target:
                    break
                if not (bit_mask & (1 << j)):
                    if acc + nums[j] == target:
                        if count + 1 == k - 1:
                            return True
                        return dfs(0, 0, bit_mask | (1 << j), count + 1)
                    else:
                        if dfs(j + 1, acc + nums[j], bit_mask | (1 << j), count):
                            return True
            false_masks.add(bit_mask)
            return False

        if k == 1:
            return True
        nums.sort()
        summ = sum(nums)
        n = len(nums)
        target, r = divmod(summ, k)
        if r:
            return False
        false_masks = set()
        return dfs(0, 0, 0, 0)
