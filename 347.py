from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def kselect(low: int, high: int) -> [int]:
            start = low
            end = high
            low += 1
            while low <= high:
                if nums_count[unique[low]] < nums_count[unique[start]]:
                    unique[low], unique[high] = unique[high], unique[low]
                    high -= 1
                else:
                    low += 1
            unique[start], unique[low - 1] = unique[low - 1], unique[start]
            if low - 1 <= k <= low:
                return unique[:k]
            elif k < low - 1:
                return kselect(start, low - 2)
            else:
                return kselect(low, end)

        nums_count = Counter(nums)
        unique = list(nums_count.keys())
        return kselect(0, len(unique) - 1)


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums))]
        nums = Counter(nums)
        for n, v in nums.items():
            bucket[v - 1].append(n)
        return [i for b in bucket for i in b][-k:]


print(Solution().topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
