import turtle

RED = 1
BLACK = 0


class Node:
    def __init__(self, key: int, val: int = 0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
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


def insert(node: Node, key: int, val: int = 0) -> Node:
    if not node:
        return Node(key, val)
    if key == node.key:
        node.val = val
    elif key < node.key:
        node.left = insert(node.left, key, val)
    else:
        node.right = insert(node.right, key, val)
    if isRed(node.right) and not isRed(node.left):
        node = rotateLeft(node)
    if isRed(node.left) and isRed(node.left.left):
        node = rotateRight(node)
    if isRed(node.left) and isRed(node.right):
        flipColors(node)
    return node


def drawTree(root: Node):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 10, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


# root = None
# for i in range(100):
#     root = insert(root, i, i)
#     root.color = BLACK
# drawtree(root)
class RedBlackTree:
    def __init__(self):
        pass

    def insert(self, n: int) -> Node:
        pass

    def getMin(self) -> int:
        pass

    def getMax(self) -> int:
        pass

    def remove(self, n: int) -> Node:
        pass


xtree = RedBlackTree()
ytree = RedBlackTree()
p2c = dict()
x2c = dict()
y2c = dict()


def addPoint(x: int, y: int):
    if (x, y) not in p2c:
        p2c[x, y] = 0
    p2c[x, y] += 1
    if x not in x2c:
        x2c[x] = 0
        xtree.insert(x)
    x2c[x] += 1
    if y not in y2c:
        y2c[y] = 0
        ytree.insert(y)
    y2c[y] += 1
    return xtree.getMin(), xtree.getMax(), ytree.getMin(), ytree.getMax()


def removePoint(x: int, y: int):
    assert p2c[x, y] > 0
    p2c[x, y] -= 1
    if p2c[x, y] == 0:
        del p2c[x, y]
    x2c[x] -= 1
    if x2c[x] == 0:
        del x2c[x]
        xtree.remove(x)
    y2c[y] -= 1
    if y2c[y] == 0:
        del y2c[y]
        ytree.remove(y)
    if not p2c:
        return None
    return xtree.getMin(), xtree.getMax(), ytree.getMin(), ytree.getMax()
