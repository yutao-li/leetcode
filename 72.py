class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # op[i1,i2]: # of op to match the first i1 letters and first i2 letters
        op = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        op[0] = [i for i in range(len(word2) + 1)]
        for i in range(len(word1) + 1):
            op[i][0] = i
        for i1 in range(1, len(word1) + 1):
            for i2 in range(1, len(word2) + 1):
                if word1[i1 - 1] == word2[i2 - 1]:
                    op[i1][i2] = op[i1 - 1][i2 - 1]
                else:
                    op[i1][i2] = 1 + min(op[i1 - 1][i2 - 1], op[i1 - 1][i2], op[i1][i2 - 1])
        return op[len(word1)][len(word2)]


word1 = "intention"
word2 = "execution"
print(Solution().minDistance(word1, word2))
