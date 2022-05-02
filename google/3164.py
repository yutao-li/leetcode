from collections import defaultdict


class Node:
    def __init__(self):
        self.left = None
        self.right = None


def countChains(root):
    def countFromNode(node, length):
        if node.left:
            if node.right:
                counter[length] += 1
                countFromNode(node.left, 0)
                countFromNode(node.right, 0)
            else:
                countFromNode(node.left, length + 1)
        else:
            if node.right:
                countFromNode(node.right, length + 1)
            elif length:
                counter[length] += 1

    counter = defaultdict(int)
    countFromNode(root, 0)
    return counter
