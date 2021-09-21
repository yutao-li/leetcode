from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if not nums1:
            q, r = divmod(len(nums2), 2)
            return nums2[q] if r else (nums2[q] + nums2[q - 1]) / 2
        q, r = divmod(len(nums1) + len(nums2), 2)
        if nums1[-1] <= nums2[0]:
            if len(nums1) == len(nums2):
                return (nums1[-1] + nums2[0]) / 2
            else:
                shifted = q - len(nums1)
                return nums2[shifted] if r else (nums2[shifted] + nums2[shifted - 1]) / 2
        if nums2[-1] <= nums1[0]:
            if len(nums1) == len(nums2):
                return (nums2[-1] + nums1[0]) / 2
            else:
                return nums2[q] if r else (nums2[q] + nums2[q - 1]) / 2
        low, high = -1, len(nums1)
        while True:
            i1 = (low + high) // 2
            i2 = q - 1 - i1
            if i1 == -1:
                if nums1[0] >= nums2[i2]:
                    return nums2[i2] if r else (nums2[i2] + nums2[i2 - 1]) / 2
                else:
                    low = 0
            elif i2 == -1:
                if nums2[0] >= nums1[i1]:
                    return nums1[i1] if r else (nums1[i1] + nums1[i1 - 1]) / 2
                else:
                    high = i1
            elif nums1[i1] == nums2[i2]:
                return nums1[i1]
            elif nums1[i1] < nums2[i2]:
                if i1 + 1 >= len(nums1) or nums2[i2] <= nums1[i1 + 1]:
                    pre = max(nums1[i1], nums2[i2 - 1]) if i2 - 1 >= 0 else nums1[i1]
                    return nums2[i2] if r else (nums2[i2] + pre) / 2
                else:
                    low = i1 + 1
            else:
                if i2 + 1 >= len(nums2) or nums1[i1] <= nums2[i2 + 1]:
                    pre = max(nums2[i2], nums1[i1 - 1]) if i1 - 1 >= 0 else nums2[i2]
                    return nums1[i1] if r else (nums1[i1] + pre) / 2
                else:
                    high = i1


print(Solution().findMedianSortedArrays([4], [1, 2, 3, 5]))
