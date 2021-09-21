class Node:
    def __init__(self, key, value):
        self.pre = None
        self.next = None
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.di = dict()
        self.counter = 0
        self.h_key = None
        self.b_key = None

    def get(self, key: int) -> int:
        if key not in self.di:
            return -1
        else:
            cur_node = self.di[key]
            if self.h_key != key:
                next_node = cur_node.next
                pre_node = cur_node.pre
                if next_node:
                    next_node.pre = pre_node
                else:
                    self.b_key = pre_node.key
                pre_node.next = next_node
                head = self.di[self.h_key]
                head.pre = cur_node
                cur_node.pre = None
                cur_node.next = head
                self.h_key = key
            return cur_node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.di:
            if self.capacity > 1:
                if self.counter == self.capacity:
                    second = self.di[self.b_key].pre
                    second.next = None
                    del self.di[self.b_key]
                    self.b_key = second.key
                    self.counter -= 1
                tmp = Node(key, value)
                self.counter += 1
                self.di[key] = tmp
                if self.h_key is not None:
                    tmp.next = self.di[self.h_key]
                    self.di[self.h_key].pre = tmp
                else:
                    self.b_key = key
                self.h_key = key
            else:
                self.h_key = self.b_key = key
                self.di = {key: Node(key, value)}
        else:
            self.di[key].value = value
            self.get(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LRUCache(1)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)  # returns 1
cache.put(3, 3)  # evicts key 2
cache.get(2)  # returns -1 (not found)
cache.put(4, 4)  # evicts key 1
cache.get(1)  # returns -1 (not found)
cache.get(3)  # returns 3
cache.get(4)  # returns 4
