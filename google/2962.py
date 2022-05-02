import turtle
from collections import defaultdict


class Node:
    def __init__(self, val='*', left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def huffmanTree(mapping: {str: int}) -> Node:
    if not mapping:
        return None
    l2c = defaultdict(list)
    for ch, l in mapping.items():
        l2c[l].append(ch)
    for k, v in l2c.items():
        v.sort()
        l2c[k] = [Node(ch) for ch in v]
    max_path = max(l2c)
    for depth in range(max_path - 1, -1, -1):
        next_layer = l2c[depth + 1]
        assert len(next_layer) % 2 == 0
        for i in range(0, len(next_layer), 2):
            l2c[depth].append(Node('*', next_layer[i], next_layer[i + 1]))
    assert len(l2c[0]) == 1
    return l2c[0][0]


node = huffmanTree({'b': 3, 'z': 3, 'a': 3, 'c': 3, 'b1': 3, 'z1': 3, 'a1': 3, 'c1': 3})


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


drawTree(node)
