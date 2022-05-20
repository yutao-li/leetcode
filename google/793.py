from bisect import bisect_right, bisect_left


class Node:
    def getText(self) -> str:
        pass

    def getChildren(self) -> ['Node']:
        pass

    def getParent(self) -> 'Node':
        pass

    def isText(self) -> bool:
        pass


def findFirstMatch(text, target) -> int:
    pass


def findText(root, searchString):
    def traverse(node):
        nonlocal curIndex
        if node.isText:
            wholeText.append(node.getText())
            index2node[curIndex] = node
            indices.append(curIndex)
            curIndex += len(node.getText())
        else:
            for child in node.getChildren():
                traverse(child)

    wholeText = []
    indices = []
    curIndex = 0
    index2node = dict()
    traverse(root)
    wholeText = ''.join(wholeText)
    startI = findFirstMatch(wholeText, searchString)
    start = bisect_left(indices, startI)
    endI = startI + len(searchString)
    end = bisect_right(indices, endI)
    return [index2node[i] for i in indices[start: end]]
