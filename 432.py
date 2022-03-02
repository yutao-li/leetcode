class KeysNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.keys = set()


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key2count = dict()
        self.count2keys = dict()
        self.head = KeysNode()  # largest
        self.tail = KeysNode()  # smallest
        self.head.right = self.tail
        self.tail.left = self.head

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.key2count:
            cur_node = self.count2keys[self.key2count[key]]
            cur_node.keys.remove(key)
            self.key2count[key] += 1
            value = self.key2count[key]
            if value in self.count2keys:
                self.count2keys[value].keys.add(key)
            else:
                left_node = cur_node.left
                new_node = KeysNode(left_node, cur_node)
                new_node.keys.add(key)
                self.count2keys[value] = new_node
                left_node.right = new_node
                cur_node.left = new_node
            if not cur_node.keys:
                left_node = cur_node.left
                right_node = cur_node.right
                left_node.right = right_node
                right_node.left = left_node
                del self.count2keys[value - 1]
        else:
            self.key2count[key] = 1
            if 1 not in self.count2keys:
                left_node = self.tail.left
                new_node = KeysNode(left_node, self.tail)
                self.count2keys[1] = new_node
                left_node.right = new_node
                self.tail.left = new_node
            self.count2keys[1].keys.add(key)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's count is 1, remove it from the data structure.
        """
        count = self.key2count[key]
        cur_node = self.count2keys[count]
        self.key2count[key] -= 1
        if self.key2count[key] == 0:
            del self.key2count[key]
        else:
            if count - 1 not in self.count2keys:
                right_node = cur_node.right
                new_node = KeysNode(cur_node, right_node)
                self.count2keys[count - 1] = new_node
                right_node.left = new_node
                cur_node.right = new_node
            self.count2keys[count - 1].keys.add(key)
        cur_node.keys.remove(key)
        if not cur_node.keys:
            right_node = cur_node.right
            left_node = cur_node.left
            right_node.left = left_node
            left_node.right = right_node
            del self.count2keys[count]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return next(iter(self.head.right.keys)) if self.key2count else ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(iter(self.tail.left.keys)) if self.key2count else ''


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc('a')
obj.inc('b')
obj.inc('b')
obj.inc('c')
obj.inc('c')
obj.inc('c')
obj.dec('b')
obj.dec('b')
print(obj.getMinKey())
obj.dec('a')
print(obj.getMaxKey())
print(obj.getMinKey())
