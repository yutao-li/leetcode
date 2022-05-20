class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class TreeMap:
    def get(self, key) -> int:
        pass

    def set(self, key, value):
        pass

    def upperBound(self, key) -> int:
        pass

    def lowerBound(self, key) -> int:
        pass

    def remove(self, key):
        pass

    def next(self, key) -> int:
        '''
        returns None when reaches the end
        :param key:
        :return:
        '''
        pass

    def prev(self, key):
        '''
        returns None when reaches the beginning
        :param key:
        :return:
        '''
        pass


treeMap = TreeMap()


def getPaintedAreaEachDay(segments):
    if not segments:
        return []
    paintedAreas = []
    for segment in segments:
        start = segment.start
        end = segment.end
        prev = treeMap.upperBound(start)
        if prev and treeMap.get(prev) > start:
            start = prev
            left = treeMap.get(prev)
        else:
            left = start
        area = end - left
        nextKey = treeMap.next(start)
        while nextKey and nextKey <= end:
            area -= min(end, treeMap.get(nextKey)) - nextKey
            end = max(end, treeMap.get(nextKey))
            newKey = treeMap.next(nextKey)
            treeMap.remove(nextKey)
            nextKey = newKey
        treeMap.set(start, end)
        paintedAreas.append(max(0, area))
    return paintedAreas


def removePaint(segment):
    key = segment.start
    value = segment.end
    prev = treeMap.upperBound(key)
    if prev and treeMap.get(prev) > key:
        treeMap.set(prev, value)
    nextKey = treeMap.lowerBound(key)
    while nextKey and treeMap.get(nextKey) <= value:
        newKey = treeMap.next(nextKey)
        treeMap.remove(nextKey)
        nextKey = newKey
    if nextKey:
        right = treeMap.get(nextKey)
        treeMap.remove(nextKey)
        treeMap.set(value, right)
