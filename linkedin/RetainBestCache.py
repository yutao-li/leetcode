from collections import defaultdict
from heapq import heappush, heappop


class DataSource:
    def get(self, key: int) -> int:
        pass

    def getRank(self, key: int) -> int:
        pass


class RetainBestCache:
    def __init__(self, dataSource: DataSource, capacity: int):
        self.pq = []
        self.rank_to_key = defaultdict(list)
        self.key_to_val = dict()
        self.capacity = capacity
        self.dataSource = dataSource

    def get(self, key: int) -> int:
        if key in self.key_to_val:
            return self.key_to_val[key]
        else:
            val = self.dataSource.get(key)
            self.key_to_val[key] = val
            rank = self.dataSource.get(key)
            self.rank_to_key[rank].append(key)
            heappush(self.pq, rank)
            if len(self.key_to_val) > self.capacity:
                rank = heappop(self.pq)
                key = self.rank_to_key[rank].pop()
                del self.key_to_val[key]
            return val
