class Iterator:
    def next(self):
        pass

    def closed(self):
        pass


class Redactor:
    def __init__(self, bannedWordsIter, toRedactIter):
        def constructTrie():
            trie = dict()
            while True:
                try:
                    word = next(bannedWordsIter)
                    next(bannedWordsIter)
                except StopIteration:
                    return trie
                if not word:
                    return trie
                node = trie
                for ch in word:
                    if ch not in node:
                        node[ch] = dict()
                    node = node[ch]
                node[0] = 1

        bannedWordsIter = self.nextToken(bannedWordsIter)
        toRedactIter = self.nextToken(toRedactIter)
        self.trie = constructTrie()
        self.toRedact = toRedactIter

    def nextToken(self, iterator):
        word = []
        while not iterator.closed():
            ch = iterator.next()
            if not ch.isalpha():
                yield ''.join(word)
                yield ch
                word = []
            else:
                word.append(ch)
        if word:
            yield ''.join(word)

    def redact(self):
        def match(word):
            node = self.trie
            for ch in word:
                if ch not in node:
                    return False
                node = node[ch]
            return 0 in node

        while True:
            word = next(self.toRedact)
            if not word.isalpha():
                yield word
            else:
                if match(word.lower()):
                    yield '_REDACTED_'
                else:
                    yield word
