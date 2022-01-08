from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {}
        for i, n in enumerate(nums):
            if n:
                self.d[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in self.d.keys() & vec.d.keys():
            res += self.d[i] * vec.d[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
