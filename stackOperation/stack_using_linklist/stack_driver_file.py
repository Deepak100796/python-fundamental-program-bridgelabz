"""
importing statement
"""
from dataStructureProgram.stackOperation.stack_using_linklist.stackMethods import Node,LinkedList

# # @creating object of LinkedList()
# myList = LinkedList()
# print("Inserting")

# @ calling all method from LinkedList
# myList.addNode(5)
# myList.addNode(15)
# myList.addNode(25)
# print("Printing")
# myList.printNode()
# # print("Size")
# print("size" , myList.getSize())

myList = LinkedList()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    print("size")
    print("print")
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'push':
        myList.push((do[1]))
    elif operation == 'pop':
        print('POP value: ', myList.pop())
    elif operation == 'print':
        print(myList.printNode())
    elif operation == "size":
        print(myList.size())
    elif operation == 'quit':
        break