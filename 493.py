from bisect import bisect_right


class Solution:
    def reversePairs(self, nums):
        def divide(nums):
            if len(nums) == 1:
                return nums, 0
            mid = len(nums) // 2
            l1, c1 = divide(nums[:mid])
            l2, c2 = divide(nums[mid:])
            double = [2 * i for i in l2]
            count = c1 + c2
            i = bisect_right(l1, double[0])
            for d in double:
                i = bisect_right(l1, d, i)
                if i == len(l1):
                    break
                count += len(l1) - i
            return sorted(l1 + l2), count

        if not nums:
            return 0
        return divide(nums)[1]


nums = []
print(Solution().reversePairs(nums))
