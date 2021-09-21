# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


import json


class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

        def helper(node):

            if node.children:
                res = [node.val]
                for child in node.children:
                    res.append(helper(child))
            else:
                res = node.val
            return res

        if not root:
            return ''
        else:
            return str(helper(root))

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

        def helper(arr):
            root = Node(arr[0], [])
            for child in arr[1:]:
                if type(child) is int:
                    root.children.append(Node(child,[]))
                else:
                    root.children.append(helper(child))
            return root

        if not data:
            return
        elif data.isnumeric():
            return Node(int(data), [])
        else:
            data = json.loads(data)
            return helper(data)


# Your Codec object will be instantiated and called as such:
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
codec = Codec()
codec.deserialize(codec.serialize(root))
