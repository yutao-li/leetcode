class Solution:
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if len(A) == 1:
            return [1]
        if A[-1] == -1:
            return []
        coins = [0] * (len(A) + 1)
        forward = [0] * (len(A))
        for i in range(len(A) - 1, 0, -1):
            minIndex = -1
            minV = float('inf')
            for j in range(1, min(len(A) - i, B) + 1):
                if A[i + j - 1] != -1:
                    coin = coins[i + j] + A[i + j - 1]
                    if coin < minV:
                        minV = coin
                        minIndex = i + j
            forward[i] = minIndex
            coins[i] = minV
        if coins[1] == float('inf'):
            return []
        else:
            res = [1]
            i = 1
            while i != len(A):
                i = forward[i]
                res.append(i)
            return res


A, B = [1,2,4,-1,2], 1
print(Solution().cheapestJump(A, B))
