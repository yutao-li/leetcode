import bisect
from collections import Counter, deque, defaultdict
from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        counter = Counter(nums)
        res = []
        if 0 in counter and counter[0] >= 3:
            res.append((0, 0, 0))
            counter[0] = 1
        for k, v in counter.items():
            if k != 0 and v >= 2 and -2 * k in counter:
                res.append((-2 * k, k, k))
        if len(counter) < 3:
            return res

        nums = sorted(list(counter))
        front = 0
        end = len(nums) - 1
        queue = deque([(front, end)])
        visited = {(front, end)}

        while queue:
            front, end = queue.popleft()
            tsum = -(nums[front] + nums[end])
            if nums[front] < tsum < nums[end]:
                if tsum in counter:
                    res.append([tsum, nums[front], nums[end]])
                if front < end - 1:
                    if (front, end - 1) not in visited:
                        queue.append((front, end - 1))
                        visited.add((front, end - 1))
                    if (front + 1, end) not in visited:
                        queue.append((front + 1, end))
                        visited.add((front + 1, end))
            else:
                if tsum <= nums[front]:
                    end = bisect.bisect_left(nums, -(nums[front] + nums[front + 1]), front + 1, end)
                else:
                    front = bisect.bisect_left(nums, -(nums[end] + nums[end - 1]), front + 1, end)
                if front < end and (front, end) not in visited:
                    queue.append((front, end))
                    visited.add((front, end))
        return res


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums = sorted(counter)
        two_sum = defaultdict(list)
        res = []
        for i, n in enumerate(nums):
            res += [comb + [n] for comb in two_sum[-n]]
            c = counter[n]
            if c >= 2:
                if -2 * n in counter and n > 0:
                    res.append([-2 * n, n, n])
                two_sum[n * 2].append([n] * 2)
            if c >= 3 and n == 0:
                res.append([0, 0, 0])
            for j in nums[:i]:
                two_sum[j + n].append([j, n])
        return res


inpu = [1, 1, -2]
print(Solution1().threeSum(inpu))
