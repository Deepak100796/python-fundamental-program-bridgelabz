"""
Number of Binary Search Tree
Solve the Problem in the following link
https://www.hackerrank.com/challenges/number­of­binary­search­tree .
"""

class Node:

    def __init__(self,data):
        self.left_child = None
        self.right_child = None
        self.data = data

    def insertion(self,data):
        if self.data == None:
            self.data = Node(data)
        elif data < self.data:
            if self.left_child == None :
                self.left_child = Node(data)
            else:
                self.left_child.insertion(data)
        elif data > self.data:
            if self.right_child == None:
                self.right_child = Node(data)
            else:
                self.right_child.insertion(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left_child:
            self.left_child.PrintTree()
        print(self.data),
        if self.right_child:
            self.right_child.PrintTree()


# @driver code
tree = Node(3)
list = [3]
for i in range(len(list)):
    tree.insertion(list[i])
tree.PrintTree()
