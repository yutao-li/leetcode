class Node:
    def __init__(self, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.keys = set()


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.k2v = dict()
        self.v2n = dict()
        self.top = None
        self.bottom = None

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.k2v:
            cur_node = self.v2n[self.k2v[key]]
            cur_node.keys.remove(key)
            self.k2v[key] += 1
            value = self.k2v[key]
            if value in self.v2n:
                self.v2n[value].keys.add(key)
            else:
                self.v2n[value] = Node(cur_node, cur_node.next)
                next_node = self.v2n[value]
                next_node.keys.add(key)
                if cur_node.next:
                    cur_node.next.prev = next_node
                cur_node.next = next_node
            if not cur_node.keys:
                pre_node = cur_node.prev
                next_node = self.v2n[value]
                if pre_node:
                    pre_node.next = next_node
                next_node.prev = pre_node
                del self.v2n[value - 1]
                if self.bottom == cur_node:
                    self.bottom = next_node
            if self.top == cur_node:
                self.top = self.v2n[value]
        else:
            self.k2v[key] = 1
            if 1 not in self.v2n:
                self.v2n[1] = Node(None, self.bottom)
            self.v2n[1].keys.add(key)
            if not self.bottom:
                self.bottom = self.v2n[1]
                self.top = self.v2n[1]
            else:
                self.bottom.prev = self.v2n[1]
                self.bottom = self.v2n[1]

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.k2v:
            value = self.k2v[key]
            cur_node = self.v2n[value]
            cur_node.keys.remove(key)
            if value > 1:
                self.k2v[key] -= 1
                if value - 1 not in self.v2n:
                    pre_node = cur_node.prev
                    self.v2n[value - 1] = Node(pre_node, cur_node)
                    if pre_node:
                        pre_node.next = self.v2n[value - 1]
                    cur_node.prev = self.v2n[value - 1]
                self.v2n[value - 1].keys.add(key)
                if not cur_node.keys:
                    pre_node = self.v2n[value - 1]
                    next_node = cur_node.next
                    pre_node.next = next_node
                    if next_node:
                        next_node.prev = pre_node
                    del self.v2n[value]
                    if self.top == cur_node:
                        self.top = pre_node
                if self.bottom == cur_node:
                    self.bottom = self.v2n[value - 1]
            else:
                del self.k2v[key]
                if not cur_node.keys:
                    next_node = cur_node.next
                    next_node.prev = None
                    del self.v2n[1]
                    self.bottom = next_node
                    if self.top == cur_node:
                        self.top = None

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return next(iter(self.top.keys)) if self.k2v else ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return next(iter(self.bottom.keys)) if self.k2v else ''


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
