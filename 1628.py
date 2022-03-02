from abc import ABC, abstractmethod
from typing import List

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class ExpTreeNode(Node):
    def __init__(self, rightChild, leftChild, val):
        self.left = leftChild
        self.right = rightChild
        self.val = val

    def evaluate(self) -> int:
        if not self.left:
            return int(self.val)
        leftVal = self.left.evaluate()
        rightVal = self.right.evaluate()
        if self.val == '+':
            return leftVal + rightVal
        elif self.val == '-':
            return leftVal - rightVal
        elif self.val == '*':
            return leftVal * rightVal
        else:
            return leftVal // rightVal


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""
operators = ('+', '-', '*', '/')


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for exp in postfix:
            if exp in operators:
                stack.append(ExpTreeNode(stack.pop(), stack.pop(), exp))
            else:
                stack.append(ExpTreeNode(None, None, exp))
        return stack[0]


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
