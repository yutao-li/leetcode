class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = dict(zip(keyboard, range(len(keyboard))))
        return sum(abs(pos[i] - pos[j]) for i, j in zip(word, word[1:])) + pos[word[0]]


res = Solution().calculateTime(keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode")

