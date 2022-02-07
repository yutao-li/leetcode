from heapq import heappush, heappop


class Node:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val

    def __lt__(self, other):
        return self.val >= other.val


class MaxStack:

    def __init__(self):
        self.heap = []
        self.tail = Node(None, None, 0)

    def push(self, x: int) -> None:
        pre = self.tail.left
        n = Node(pre, self.tail, x)
        if pre:
            pre.right = n
        self.tail.left = n
        heappush(self.heap, n)

    def pop(self) -> int:
        n = self.tail.left
        pre = n.left
        if pre:
            pre.right = self.tail
        self.tail.left = pre
        n.right = None
        return n.val

    def top(self) -> int:
        return self.tail.left.val

    def peekMax(self) -> int:
        n = self.heap[0]
        while not n.right:
            heappop(self.heap)
            n = self.heap[0]
        return n.val

    def popMax(self) -> int:
        n = heappop(self.heap)
        while not n.right:
            n = heappop(self.heap)
        pre = n.left
        post = n.right
        if pre:
            pre.right = post
        post.left = pre
        return n.val

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
