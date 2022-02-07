from bisect import bisect_left
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count(a, b, mid):
            if not a or not b:
                return 0
            r = len(b) - 1
            res = 0
            for i in a:
                while r > -1 and b[r] * i > mid:
                    r -= 1
                if r < 0:
                    break
                res += r + 1
            return res

        low = -10 ** 10
        high = 10 ** 10
        n1 = len(nums1)
        n2 = len(nums2)
        i1 = bisect_left(nums1, 0)
        i2 = bisect_left(nums2, 0)
        neg1, pos1 = nums1[:i1], nums1[i1:]
        neg2, pos2 = nums2[:i2], nums2[i2:]
        neg1_r, pos1_r = neg1[::-1], pos1[::-1]
        neg2_r, pos2_r = neg2[::-1], pos2[::-1]
        neg = i1 * (n2 - i2) + i2 * (n1 - i1)
        if not neg:
            low = 0
        while low < high:
            mid = (low + high) // 2
            if mid >= 0:
                rank = neg + count(neg1_r, neg2_r, mid) + count(pos1, pos2, mid)
            else:
                rank = count(pos1_r, neg2, mid) + count(pos2_r, neg1, mid)
            if rank >= k:
                high = mid
            else:
                low = mid + 1
        return low


print(Solution().kthSmallestProduct(nums1=[-2, -1, 0, 1, 2], nums2=[-3, -1, 2, 4, 5], k=3))
