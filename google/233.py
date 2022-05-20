from collections import OrderedDict


class LruCache:
    def __init__(self, size):
        self.size = size
        self.cache = OrderedDict()

    def addSearchString(self, searchString):
        if searchString in self.cache:
            self.cache.move_to_end(searchString)
        else:
            if len(self.cache) == self.size:
                self.cache.popitem(False)
            self.cache[searchString] = 1

    def getRecommendations(self):
        return list(reversed(self.cache))


lruCache = LruCache(3)
lruCache.addSearchString('a')
lruCache.addSearchString('b')
lruCache.addSearchString('c')
lruCache.addSearchString('b')
lruCache.addSearchString('d')
print(lruCache.getRecommendations())
