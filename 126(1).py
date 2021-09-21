import collections
import string


class Solution:
    def findLadders(self, beginWord, endWord, wordList):

        if endWord not in wordList or not beginWord or not endWord:
            return []
        wordList = set(wordList)
        parents = collections.defaultdict(set)
        forward, backward = {beginWord}, {endWord}
        direction = 1
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                direction *= -1
            nextForward = set()
            wordList -= forward
            for w in forward:
                for i in range(len(w)):
                    first, second = w[:i], w[i + 1:]
                    for ch in string.ascii_lowercase:
                        combinedWord = first + ch + second
                        if combinedWord in wordList:
                            nextForward.add(combinedWord)
                            if direction == 1:
                                parents[combinedWord].add(w)
                            else:
                                parents[w].add(combinedWord)
            forward = nextForward
            if nextForward & backward:
                self.res = []
                path = [endWord]
                self.dfs(parents, endWord, beginWord, path)
                return self.res
        return []

    def dfs(self, parents, cur_w, beginWord, path):
        if cur_w == beginWord:
            self.res.append(path[::-1])
            return
        for eword in parents[cur_w]:
            path.append(eword)
            self.dfs(parents, eword, beginWord, path)
            path.pop()


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
res = Solution().findLadders(beginWord, endWord, wordList)
