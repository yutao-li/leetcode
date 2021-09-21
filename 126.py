from collections import defaultdict
from typing import *


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def dfs(previous, acc: list, terminal, paths):
            if acc[-1] == terminal:
                paths.append(list(acc))
                return
            for word in previous[acc[-1]]:
                acc.append(word)
                dfs(previous, acc, terminal, paths)
                acc.pop()

        wordList = set(wordList)
        nodes = defaultdict(list)
        if endWord not in wordList:
            return []
        for word in wordList:
            for i in range(len(word)):
                nodes[word[:i] + '*' + word[i + 1:]].append(word)
        queue_left = {beginWord}
        queue_right = {endWord}

        previous_left = defaultdict(list)
        previous_right = defaultdict(list)
        forward = True
        while queue_left and queue_right:
            queue = set()
            wordList -= queue_left
            for word in queue_left:
                for i in range(len(word)):
                    for next_word in nodes[word[:i] + '*' + word[i + 1:]]:
                        if next_word in wordList:
                            previous_left[next_word].append(word)
                            queue.add(next_word)

            connection = queue & queue_right
            if connection:
                if not forward:
                    previous_left, previous_right = previous_right, previous_left
                paths = []
                for node in connection:
                    paths_left = []
                    dfs(previous_left, [node], beginWord, paths_left)
                    paths_right = []
                    dfs(previous_right, [node], endWord, paths_right)
                    for i in paths_left:
                        for j in paths_right:
                            paths.append(i[::-1] + j[1:])
                return paths
            queue_left, queue_right = queue_right, queue
            previous_left, previous_right = previous_right, previous_left
            forward = not forward
        return []


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
res = Solution().findLadders(beginWord, endWord, wordList)
