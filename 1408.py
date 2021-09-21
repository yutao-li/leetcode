from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ss = set()
        for word in words:
            for dist in range(1, len(word)):
                for i in range(len(word) - dist + 1):
                    ss.add(word[i:i + dist])
        res = []
        for word in words:
            if word in ss:
                res.append(word)
        return res


print(Solution().stringMatching(["blue","green","bu"]))
