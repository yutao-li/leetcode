from bisect import bisect_left


class Solution:
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        N = str(N)
        amount = 0
        C = 1
        size = len(D)
        for k in range(1, len(N)):
            C = C * size
            amount += C
        return amount + self.count(D, N, 0)

    def count(self, D: list, N, index):
        if index == len(N):
            return 1
        di = N[index]
        num = bisect_left(D, di)
        amount = num * (len(D) ** (len(N) - index - 1))
        if num < len(D) and D[num] == di:
            amount += self.count(D, N, index + 1)
        return amount


D = ["7"]
N = 8
print(Solution().atMostNGivenDigitSet(D, N))
