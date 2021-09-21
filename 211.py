class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.di = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tmp = self.di
        for ch in word:
            if ch not in tmp:
                tmp[ch] = dict()
            tmp = tmp[ch]
        tmp['.'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def dfs(word, di):
            if not word:
                return '.' in di
            if word[0] == '.':
                for sub_di in di.values():
                    if sub_di is not True:
                        found = dfs(word[1:], sub_di)
                        if found:
                            return True
                return False
            elif word[0] in di:
                return dfs(word[1:], di[word[0]])

        return dfs(word, self.di)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
obj.search("pad")
obj.search("b..")
obj.search("bad")
obj.search(".ad")
