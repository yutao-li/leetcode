class Solution:
    def countRangeSum(self, nums, lower, upper):
        def divide(sums):
            if len(sums) == 1:
                return sums, int(lower <= sums[0] <= upper)
            mid = len(sums) // 2
            l1, c1 = divide(sums[:mid])
            l2, c2 = divide(sums[mid:])

            lowerInd = 0
            upperInd = 0
            count = c1 + c2
            for s in l1:
                while lowerInd < len(l2) and l2[lowerInd] - s < lower:
                    lowerInd += 1
                if lowerInd == len(l2):
                    break
                upperInd = max(lowerInd, upperInd)
                while upperInd < len(l2) and l2[upperInd] - s <= upper:
                    upperInd += 1
                count += upperInd - lowerInd
            return sorted(l1 + l2), count

        if not nums:
            return 0
        sums = []
        s = 0
        for num in nums:
            s += num
            sums.append(s)
        return divide(sums)[1]


print(Solution().countRangeSum([-2, 5, -1], -2, 2))
