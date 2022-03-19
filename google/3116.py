from collections import defaultdict
from math import floor

RED = 1
BLACK = 0


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = RED


def isRed(node: Node) -> bool:
    if not node:
        return False
    return node.color == RED


def rotateRight(node: Node) -> Node:
    assert isRed(node.left)
    x = node.left
    node.left = x.right
    x.right = node
    x.color = BLACK
    node.color = RED
    return x


def rotateLeft(node: Node) -> Node:
    assert isRed(node.right)
    x = node.right
    node.right = x.left
    x.left = node
    x.color = node.color
    node.color = RED
    return x


def flipColors(node: Node) -> None:
    assert not isRed(node)
    assert isRed(node.left)
    assert isRed(node.right)
    node.color = RED
    node.left.color = BLACK
    node.right.color = BLACK


def insert(node: Node, val: int) -> Node:
    if not node:
        return Node(val)
    if val < node.val:
        node.left = insert(node.left, val)
        node.left.parent = node
    elif val > node.val:
        node.right = insert(node.right, val)
        node.right.parent = node
    if isRed(node.right) and not isRed(node.left):
        node = rotateLeft(node)
    if isRed(node.left) and isRed(node.left.left):
        node = rotateRight(node)
    if isRed(node.left) and isRed(node.right):
        flipColors(node)
    return node


def getSmaller(node: Node, val: int) -> int:
    smaller = None
    while node:
        if node.val < val:
            smaller = node.val
            node = node.right
        else:
            node = node.left
    return smaller


def getLarger(node: Node, val: int) -> int:
    larger = None
    while node:
        if node.val > val:
            larger = node.val
            node = node.left
        else:
            node = node.right
    return larger


root = None
for i in range(100):
    root = insert(root, i)
    root.color = BLACK

smallers = [getSmaller(root, i) for i in range(20, 50)]
largers = [getLarger(root, i) for i in range(20, 50)]

near = defaultdict(list)
d = 5
for i in range(100):
    f = floor(i / d)
    near[f].append(i)
    if len(near[f]) == 2 and near[f][0] > near[f][1]:
        near[f] = near[f][::-1]
    neighbours = near[f - 1] + near[f] + near[f + 1]
    for j, k, l in zip(neighbours, neighbours[1:], neighbours[2:]):
        if l - j <= d:
            res = [j, k, l]
            for n in res:
                near[floor(n / d)].remove(n)
            print(res)
