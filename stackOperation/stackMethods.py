"""
stack data structure.
"""
"""
    This is stack class. it include all the stack operation like push data , pop data get the size etc.
    
    @date   : 26/10/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
    
     
"""


class Stack():

    # @for constructor
    def __init__(self):
        self.items = []

    # @for checking stack is empty or not
    def isEmpty(self):
        return self.items == []

    # @for push data into the stack
    def push(self, item):
        self.items.append(item)

    # @for delete the data from stack
    def pop(self):
        return self.items.pop()

    # @for checking the last value from stack
    def peek(self):
        if (self.isEmpty):
            return "stack is empty: "
        # return self.items[len(self.items) - 1]
        return self.items[-1]

    # @checking the size of stack
    def size(self):
        return len(self.items)

    # @for printing the stack
    def get_stack(self):
        return self.items

#
# stack  =  Stack()
# stack.push(10)
# print(stack.peek())
# stack.push(20)
# stack.push(30)

# print(stack.pop())
# print(stack.peek())
