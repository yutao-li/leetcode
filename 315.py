class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums = list(enumerate(nums))
        self.count = [0] * len(nums)
        self.divide(nums)
        return self.count

    def divide(self, nums):
        if len(nums) == 1:
            return nums
        else:
            mid = len(nums) // 2
            l1 = self.divide(nums[:mid])
            l2 = self.divide(nums[mid:])
            merge = []
            i1 = 0
            i2 = 0
            while i1 < len(l1) and i2 < len(l2):
                if l1[i1][1] <= l2[i2][1]:
                    merge.append(l1[i1])
                    self.count[l1[i1][0]] += len(merge) - i1 - 1
                    i1 += 1
                else:
                    merge.append(l2[i2])
                    i2 += 1
            if i1 == len(l1):
                merge += l2[i2:]
            else:
                for i, _ in l1[i1:]:
                    self.count[i] += len(l2)
                merge += l1[i1:]
            return merge


nums = [5, 2, 6, 1]
print(Solution().countSmaller(nums))
