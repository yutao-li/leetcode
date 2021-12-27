from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        i_median, odd = divmod(len(nums1) + len(nums2), 2)
        if not nums2:
            return nums1[i_median] if odd else (nums1[i_median] + nums1[i_median - 1]) / 2
        low, high = 0, len(nums2)
        while True:
            i2 = (low + high) // 2
            i1 = i_median - i2
            n1, n2 = nums1[i1] if i1 < len(nums1) else float('inf'), nums2[i2] if i2 < len(nums2) else float('inf')
            pre1, pre2 = nums1[i1 - 1] if i1 else float('-inf'), nums2[i2 - 1] if i2 else float('-inf')
            n, pre = min(n1, n2), max(pre1, pre2)
            if n >= pre:
                return n if odd else (n + pre) / 2
            elif n1 < pre:
                high = i2 - 1
            else:
                low = i2 + 1


print(Solution().findMedianSortedArrays([100001], [100000]))
