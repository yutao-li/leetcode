from collections import defaultdict


class Node:
    def __init__(self, phoneNum=None, name=None, left=None, right=None):
        self.left = left
        self.right = right
        self.phoneNum = phoneNum
        self.name = name


class Restaurant:
    def hasTable(self, size):
        pass

    def serve(self, phoneNum, name):
        pass


class RestaurantWaitlist:
    def __init__(self, restaurant):
        def createHeadAndTail():
            head = Node()
            tail = Node()
            head.right = tail
            tail.left = head
            return head, tail

        self.contact2node = dict()
        self.size2queue = defaultdict(createHeadAndTail)
        self.restaurant = restaurant

    def join(self, phoneNum, name, size):
        if self.restaurant.hasTable(size):
            self.restaurant.serve(phoneNum, name)
            return True
        if (phoneNum, name) in self.contact2node:
            raise ValueError('already joined')
        tail = self.size2queue[size][1]
        prevNode = tail.left
        newNode = Node(phoneNum, name, prevNode, tail)
        tail.left = newNode
        prevNode.right = newNode
        self.contact2node[phoneNum, name] = newNode
        return True

    def serve(self, size):
        head, tail = self.size2queue[size]
        if head.right == tail:
            raise ValueError('empty queue')
        first = head.right
        second = first.right
        head.right = second
        second.left = head
        del self.contact2node[first.phoneNum, first.name]
        return first.phoneNum, first.name

    def quit(self, phoneNum, name):
        if (phoneNum, name) not in self.contact2node:
            raise ValueError('not joined')
        node = self.contact2node[phoneNum, name]
        left, right = node.left, node.right
        left.right, right.left = right, left
        del self.contact2node[phoneNum, name]
        return True
