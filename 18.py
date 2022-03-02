from collections import defaultdict, Counter
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        counter = Counter(nums)
        nums = sorted(counter)
        two_sum = defaultdict(list)
        three_sum = defaultdict(list)
        res = []
        for i, n in enumerate(nums):
            res += [comb + [n] for comb in three_sum[target - n]]
            for j, combs in two_sum.items():
                three_sum[j + n] += [comb + [n] for comb in combs]
            c = counter[n]
            if c >= 2:
                res += [comb + [n] * 2 for comb in two_sum[target - 2 * n]]
                two_sum[n * 2].append([n] * 2)
                for j in nums[:i]:
                    three_sum[j + 2 * n].append([j, n, n])
            if c >= 3:
                if target - 3 * n in counter and target - 3 * n < n:
                    res.append([n] * 3 + [target - 3 * n])
                three_sum[n * 3].append([n] * 3)
            if c >= 4 and n * 4 == target:
                res.append([n] * 4)
            for j in nums[:i]:
                two_sum[j + n].append([j, n])
        return res


# general version: copied
class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            # If we have run out of numbers to add, return res.
            if not nums:
                return res

            # There are k remaining values to add to the sum. The
            # average of these values is at least target // k.
            average_value = target // k

            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than target // k or if the largest
            # value in nums is smaller than target // k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res

            if k == 2:
                return twoSum(nums, target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()

            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])

            return res

        nums.sort()
        return kSum(nums, target, 4)


print(Solution().fourSum([0, 1, 5, 0, 1, 5, 5, -4], 11))
