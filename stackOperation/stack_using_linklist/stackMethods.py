"""
this is for importing module
"""
"""
    This is stack class. it include all the stack operation like push data , pop data get the size etc.

    @date   : 2/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

"""
this is Node class for creating node
"""


class Node:

    # @this is constructor:
    def __init__(self, data, nextNode=None):
        # @ initializing data and next
        self.data = data
        self.nextNode = nextNode

    # @this is getter method for data
    def getData(self):
        return self.data

    # @setter method for data
    def setData(self, val):
        self.data = val

    # @this is getter method for next
    def getNextNode(self):
        return self.nextNode

    # @this is setter method for next
    def setNextNode(self, val):
        self.nextNode = val


"""
this linked list class for implementing stack operation
"""


class LinkedList:

    # @ this constructor
    def __init__(self, head=None):
        # @initializing data and nextnode
        self.head = head
        self.size = 0

    # @ this method return size of stack
    def getSize(self):
        return self.size

    # @ this is push operation
    def push(self, data):
        # @first we create new node
        newNode = Node(data, self.head)
        # @ after that we make newNode as head
        self.head = newNode
        # @ here i increment size of linklist stack
        self.size += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.nextNode

            return popped

    # @ this method is for printing the stack
    def printNode(self):
        # @creating temperary variable for assignment head
        curr = self.head
        # @ now running loop for tracersing till end stack
        while curr:
            print(curr.data)
            curr = curr.getNextNode()
