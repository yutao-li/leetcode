class Node:
    def __init__(self, key, value, left, right):
        self.left = left
        self.right = right
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.di = dict()
        self.counter = 0
        self.head = Node(None, 0, None, None)
        self.tail = Node(None, 0, None, None)
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key: int) -> int:
        if key not in self.di:
            return -1
        else:
            node = self.di[key]
            next_node = node.right
            pre_node = node.left
            next_node.left = pre_node
            pre_node.right = next_node

            next_node = self.head.right
            next_node.left = node
            self.head.right = node
            node.left = self.head
            node.right = next_node
            return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.di:
            next_node = self.head.right
            node = Node(key, value, self.head, next_node)
            self.di[key] = node
            self.head.right = node
            next_node.left = node
            self.counter += 1
            if self.counter > self.capacity:
                self.counter -= 1
                node = self.tail.left
                pre_node = node.left
                self.tail.left = pre_node
                pre_node.right = self.tail
                del self.di[node.key]
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
