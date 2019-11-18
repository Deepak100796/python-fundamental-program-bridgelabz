"""
@ in this file I call the all the stack method from Stack class
"""
from dataStructureProgram.stackOperation.stackMethods import Stack
"""
    @import statements.
"""



"""
creating object from Stack class
"""

stack = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    print("size")
    print("print")
    print("peek")
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'push':
        stack.push((do[1]))
    elif operation == 'pop':
        if stack.isEmpty():
            print('Stack is empty.')
        else:
            print('POP value: ', stack.pop())
    elif operation == 'print':
        print(stack.get_stack())
    elif operation == "size":
        print(stack.size())
    elif operation == "peek":
        print(stack.peek())
    elif operation == 'quit':
        break


