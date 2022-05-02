class DecodingTreeNode:
    def __init__(self, letter: str, decodeString: str, children: ['DecodingTreeNode']):
        self.letter = letter
        self.decodeString = decodeString
        self.children = children


class Decoder:
    def __init__(self, decodingTree: DecodingTreeNode, inputString: str):
        self.decodingTree = decodingTree
        self.inputString = list(inputString[::-1])
        self.outputString = []
        self.isValid = True

    def next(self):
        if not self.hasNext():
            raise ValueError('no next element')
        return self.outputString.pop()

    def _findNext(self):
        node = self.decodingTree
        while not node.decodeString and self.inputString:
            child = [child for child in node.children if child.letter == self.inputString[-1]]
            if not child:
                self.isValid = False
                return
            self.inputString.pop()
            node = child[0]
        self.outputString = list(node.decodeString[::-1])

    def hasNext(self) -> bool:
        if self.outputString:
            return True
        if not self.isValid:
            return False
        if not self.inputString:
            return False
        self._findNext()
        return bool(self.outputString)
