from collections import defaultdict, Counter
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        acc1 = defaultdict(int)
        acc2 = defaultdict(int)
        for k1, v1 in Counter(nums1).items():
            for k2, v2 in Counter(nums2).items():
                acc1[k1 + k2] += v1 * v2
        for k1, v1 in Counter(nums3).items():
            for k2, v2 in Counter(nums4).items():
                acc2[k1 + k2] += v1 * v2
        return sum(v1 * acc2[-k1] for k1, v1 in acc1.items())
