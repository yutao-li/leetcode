class Node:
    def __init__(self, key, value):
        self.freq = 1
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.bottom = None
        self.cache = dict()
        self.freq2node = dict()
        self.count = 0

    def _update(self, node, prev_node):
        next_node = prev_node.next
        node.prev, node.next = prev_node, next_node
        prev_node.next = node
        if next_node:
            next_node.prev = node

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key in self.cache:
            node = self.cache[key]
            freq = node.freq
            prev_node = node.prev
            next_node = node.next
            if self.bottom == node:
                if next_node and next_node.freq <= freq + 1:
                    self.bottom = next_node
            if self.freq2node[freq] == node:
                if prev_node and prev_node.freq == freq:
                    self.freq2node[freq] = prev_node
                else:
                    del self.freq2node[freq]
                if freq + 1 in self.freq2node:
                    if prev_node:
                        prev_node.next = next_node
                    next_node.prev = prev_node
                    prev_node = self.freq2node[freq + 1]
                    self._update(node, prev_node)
            else:
                if prev_node:
                    prev_node.next = next_node
                next_node.prev = prev_node
                if freq + 1 not in self.freq2node:
                    prev_node = self.freq2node[freq]
                else:
                    prev_node = self.freq2node[freq + 1]
                self._update(node, prev_node)
            self.freq2node[freq + 1] = node
            node.freq += 1
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self.get(key)
            self.cache[key].value = value
        else:
            if self.count < self.capacity:
                self.count += 1
            else:
                bottom = self.bottom
                self.bottom = bottom.next
                del self.cache[bottom.key]
                if self.freq2node[bottom.freq] == bottom:
                    del self.freq2node[bottom.freq]
            bottom = self.bottom
            node = Node(key, value)
            if not bottom:
                self.bottom = node
            elif bottom.freq > 1:
                node.next = bottom
                bottom.prev = node
                self.bottom = node
            else:
                prev_node = self.freq2node[1]
                self._update(node, prev_node)
            self.freq2node[1] = node
            self.cache[key] = node


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)  # returns 1
cache.put(3, 3)  # evicts key 2
cache.get(2)  # returns -1 (not found)
cache.get(3)  # returns 3.
cache.put(4, 4)  # evicts key 1.
cache.get(1)  # returns -1 (not found)
cache.get(3)  # returns 3
cache.get(4)  # returns 4
