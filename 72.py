from functools import lru_cache


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # op[i1,i2]: # of op to match the first i1 letters and first i2 letters
        op = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        op[0] = list(range(len(word2) + 1))
        for i in range(len(word1) + 1):
            op[i][0] = i
        for i1 in range(1, len(word1) + 1):
            for i2 in range(1, len(word2) + 1):
                if word1[i1 - 1] == word2[i2 - 1]:
                    op[i1][i2] = op[i1 - 1][i2 - 1]
                else:
                    op[i1][i2] = 1 + min(op[i1 - 1][i2 - 1], op[i1 - 1][i2], op[i1][i2 - 1])
        return op[len(word1)][len(word2)]


class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def distance(i1, i2) -> int:
            if i2 == len(word2):
                return len(word1) - i1
            if i1 == len(word1):
                return len(word2) - i2
            if word1[i1] == word2[i2]:
                return distance(i1 + 1, i2 + 1)
            else:
                return 1 + min(distance(i1 + 1, i2 + 1), distance(i1, i2 + 1), distance(i1 + 1, i2))

        return distance(0, 0)


word1 = "intention"
word2 = "execution"
print(Solution().minDistance(word1, word2))
