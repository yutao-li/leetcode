from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        try:
            e_i = wordList.index(endWord)
        except ValueError:
            return []
        try:
            b_i = wordList.index(beginWord)
        except ValueError:
            wordList.append(beginWord)
            b_i = len(wordList) - 1
        stub = defaultdict(list)
        for i, word in enumerate(wordList):
            for j, ch in enumerate(word):
                stub[word[:j] + ' ' + word[j + 1:]].append(i)
        graph = defaultdict(list)
        for nodes in stub.values():
            for n in nodes:
                graph[n] += [i for i in nodes if i != n]
        parent = defaultdict(list)
        layer = {b_i}
        pre_layer = {}
        while e_i not in layer and layer:
            cur_layer = set()
            for i in layer:
                for j in graph[i]:
                    if j not in pre_layer and j not in layer:
                        cur_layer.add(j)
                        parent[j].append(i)
            pre_layer = layer
            layer = cur_layer
        if not layer:
            return []
        trails = [[e_i]]
        while trails[0][0] != b_i:
            trails = [[p] + n for n in trails for p in parent[n[0]]]
        return [[wordList[i] for i in t] for t in trails]


print(Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]))
