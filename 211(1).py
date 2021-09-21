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
        li = [self.di]
        for i in word:
            if i == '.':
                li = [i for j in li for i in j.values() if i is not True]
            else:
                li = [j[i] for j in li if i in j]
            if not li:
                return False
        return any('.' in i for i in li)

    # Your WordDictionary object will be instantiated and called as such:


obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

obj.addWord("a")
obj.addWord("a")
# obj.addWord("dad")
# obj.addWord("mad")
obj.search(".")
obj.search("a")
obj.search("aa")
obj.search(".a")
obj.search("a.")
