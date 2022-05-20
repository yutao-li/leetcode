# https://questions.corp.google.com/questions/3110
class Node:
    def __init__(self, left, right, parent, val):
        self.left = left
        self.right = right
        self.parent = parent
        self.val = val


directions = ('downleft', 'downright', 'upleft', 'upright')

node1 = Node(None, None, None, 1)
# node2=Node(None,None,None,2)
# node3=Node(None,None,None,3)
node4 = Node(None, None, None, 4)
node5 = Node(node1, None, None, 5)
node6 = Node(None, node4, None, 6)
node7 = Node(node5, node6, None, 7)
node1.parent = node5
# node2.parent=node5
# node3.parent=node6
node4.parent = node6
node5.parent = node7
node6.parent = node7

res = preorder_traversal(node7)
print(res)
# assert res==[7,5,1,2,6,3,4]
assert res == [7, 5, 1, 6, 4]
