from typing import *
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nodes = defaultdict(list)
        if endWord not in wordList:
            return 0
        for word in wordList:
            for i in range(len(word)):
                nodes[word[:i] + '*' + word[i + 1:]].append(word)
        visited_left = {beginWord}
        queue_left = [beginWord]
        visited_right = {endWord}
        queue_right = [endWord]
        length = 1
        while queue_left and queue_right:
            queue = []
            for word in queue_left:
                for i in range(len(word)):
                    for next_word in nodes[word[:i] + '*' + word[i + 1:]]:
                        if next_word not in visited_left:
                            if next_word in visited_right:
                                return length + 1
                            visited_left.add(next_word)
                            queue.append(next_word)
            queue_left, queue_right = queue_right, queue
            visited_left, visited_right = visited_right, visited_left
            length += 1
        return 0
