# class node for data and next
class Node(object):

    # @constructor
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    # @for get Data
    def getData(self):
        return self.data

    # @get next
    def getNext(self):
        return self.nextNode

    # @set next
    def setNext(self, newNext):
        self.nextNode = newNext


"""
class unordered linklist
"""


class UnOrderedLinklist:

    # @ for constructors
    def __init__(self):
        self.head = None

    # @add the data to the front of link list
    def add(self, item):
        # @creating the new Node
        newNode = Node(item)

        # if head is null then we have to make new node as head
        if self.head is None:
            self.head = newNode
        # @ else we have to set new node.next = head
        else:
            newNode.setNext(self.head)
            # @ now in the head we put new node
            self.head = newNode

    # for getting size
    def size(self):
        # @ initialize current as head
        current = self.head
        # @ take count = 0
        count = 0
        # iterate over until current is not null
        while current:
            count += 1
            # @every time go to next element
            current = current.getNext()
        # @ return count
        return count

    # @ for searchthe item from list
    def search(self, item):
        # @ initialize current as head
        current = self.head
        found = False

        while current and found is False:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        if current is None:
            raise ValueError("data")
        return current

    # @for delete the item from link list
    def remove(self, item):
        # @ initialize current as head and previous as null and faound as false
        current = self.head
        previous = None
        found = False

        # @iterate till current not null and found is false
        while current and found is False:
            # @ if temp.data == item then found true
            if current.getData() == item:
                found = True
            else:
                # @swap the prev to current and current to current.next
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError("Item not in the list")
        # @if previous in None then error
        if previous is None:
            self.head = current.getNext()
        else:
            # @ set the node to appropriate  position
            previous.setNext(current.getNext())

    # @for printing the list
    def printList(self):
        # @taling current as head
        current = self.head
        while current:
            print(current.getData())
            current = current.getNext()

    # @for append item in list
    def append(self, item):
        # @creating new node
        newNode = Node(item)
        newNode.setNext(None)

        # @if head is null then we have to make new node as head
        if self.head is None:
            self.head = newNode
        else:
            last = self.head
            while last.getNext():
                last = last.getNext()
            last.setNext(newNode)



# # driver code
# unorderedList = UnOrderedLinklist()
# unorderedList.add(10)
# unorderedList.add(20)
# unorderedList.add(30)
#
# unorderedList.remove(10)
# print(unorderedList.size())
#
# unorderedList.append(40)


# unorderedList.printList()
