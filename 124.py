class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.helper(root)[1]

    def helper(self, node):
        pathSum1, pathSum2, treeSum1, treeSum2 = [float('-inf')] * 4
        if node.left:
            pathSum1, treeSum1 = self.helper(node.left)
        if node.right:
            pathSum2, treeSum2 = self.helper(node.right)
        path = node.val + max(pathSum1, pathSum2, 0)
        tree = max(treeSum1, treeSum2, max(pathSum2, 0) + max(pathSum1, 0) + node.val)
        return path, tree


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    import sys
    import io
    root = stringToTreeNode("[-1,5,null,4,null,null,2,-4]")

    ret = Solution().maxPathSum(root)

    out = str(ret)
    print(out)


if __name__ == '__main__':
    main()
