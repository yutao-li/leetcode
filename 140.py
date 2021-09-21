class Solution:
    class Node:
        def __init__(self, w=False):
            self.w = w
            self.next = {}

    class Trie:
        def __init__(self):
            self.root = Solution.Node(False)
            self.memoization = {}

        def put(self, word):
            self.auxput(word, 0, self.root)

        def auxput(self, word, d, node):
            if d == len(word):
                node.w = True
            else:
                if word[d] not in node.next:
                    node.next[word[d]] = Solution.Node()
                self.auxput(word, d + 1, node.next[word[d]])

    def dfs(self, s, index, node, trie):
        if index == len(s):
            if node.w:
                return [[len(s)]]
            return []
        else:
            result = []
            if node.w:
                if index in trie.memoization:
                    result = trie.memoization[index]
                else:
                    result = self.dfs(s, index, trie.root, trie)
                    trie.memoization[index] = result
                result = [[index] + spaces for spaces in result]
            if s[index] in node.next:
                result += self.dfs(s, index + 1, node.next[s[index]], trie)
            return result

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        trie = Solution.Trie()
        for w in wordDict:
            trie.put(w)
        res = self.dfs(s, 0, trie.root, trie)
        sentences = []
        for spaces in res:
            spaces.insert(0, 0)
            sentences.append(" ".join(s[spaces[i]:spaces[i + 1]] for i in range(len(spaces) - 1)))
        return sentences


s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))
