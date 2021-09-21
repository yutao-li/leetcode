from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])
        while queue:
            tmp = queue.popleft()
            if tmp:
                queue.append(tmp.left)
                queue.append(tmp.right)
                res.append(str(tmp.val))
            else:
                res.append('null')
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = [TreeNode(int(s)) if s != 'null' else None for s in data.split()]
        pos = 1
        curNode = 0
        while pos < len(data):
            if data[curNode]:
                data[curNode].left = data[pos]
                data[curNode].right = data[pos + 1]
                pos += 2
            curNode += 1
        return data[0]


# Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.deserialize(codec.serialize(root))
