class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dp = [0] * (len(nums) - k + 1)
        largest = sum(nums[:k])
        start = 0
        acc = largest
        dp[0] = largest
        mem = [0] * (len(nums) - k + 1)
        mem[0] = largest
        pre = {(k - 1, 0): start}
        for i in range(k, len(nums)):
            acc += nums[i]
            acc -= nums[i - k]
            newStart = i - k + 1
            mem[newStart] = acc
            if largest < acc:
                largest = acc
                start = newStart
            dp[newStart] = largest
            pre[i, 0] = start

        for j in range(2, 4):
            dp[0] = dp[0] + mem[(j - 1) * k]
            pre[j * k - 1, j - 1] = (j - 1) * k
            for i in range(j * k, len(nums)):
                pos = i - j * k + 1
                hold = dp[pos] + mem[i - k + 1]
                if hold > dp[pos - 1]:
                    dp[pos] = hold
                    pre[i, j - 1] = i - k + 1
                else:
                    dp[pos] = dp[pos - 1]
                    pre[i, j - 1] = pre[i - 1, j - 1]

        res = []
        i = 2
        start = len(nums)
        while len(res) < 3:
            start = pre[start - 1, i]
            i -= 1
            res.insert(0, start)
        return res


nums = [1, 2, 1, 2, 6, 7, 5, 1]
k = 2
print(Solution().maxSumOfThreeSubarrays(nums, k))
