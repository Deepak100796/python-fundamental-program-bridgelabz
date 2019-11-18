
"""
ordered list
"""


# @node class for
class Node:
    # @ constructor
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # @ for getting data
    def getData(self):
        return self.data

    # @ for setting data
    def getNext(self):
        return self.next

    # @ for getting data
    def setData(self, newdata):
        self.data = newdata

    # @ for setting data
    def setNext(self, newnext):
        self.next = newnext


# @ orderedlist class for linklist
class OrderedList:
    # @constructor
    def __init__(self):
        self.head = None

    # @ for search data item
    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    # @ for adding data
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def print(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next


# @ driver code
# try:
#     mylist = OrderedList()
#     mylist.add(31)
#     mylist.add(77)
#     mylist.add(17)
#     mylist.add(93)
#     mylist.add(26)
#     mylist.add(54)
# except:
#     print("Enter correct input: ")
#
# print(mylist.print())
