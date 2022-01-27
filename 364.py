# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from typing import List


class Solution:
    def depthSumInverse(self, nestedList: List["NestedInteger"]) -> int:
        def maxdepth(nestedInteger):
            if nestedInteger.isInteger():
                return 1
            else:
                li = nestedInteger.getList()
                if li:
                    return 1 + max(maxdepth(i) for i in nestedInteger.getList())
                else:
                    return 0

        def dfs(nestedInteger, depth):
            if nestedInteger.isInteger():
                return nestedInteger.getInteger() * (max_depth - depth)
            else:
                li = nestedInteger.getList()
                if li:
                    return sum(dfs(i, depth + 1) for i in nestedInteger.getList())
                else:
                    return 0

        max_depth = max(maxdepth(i) for i in nestedList) + 1
        return sum(dfs(i, 1) for i in nestedList)
