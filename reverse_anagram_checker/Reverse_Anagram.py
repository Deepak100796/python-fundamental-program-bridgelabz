# @ class node
class Node:
    def __init__(self, data):
        # It creates the node with data and address fields
        self.data = data
        self.next = None


# @ class linklist
class LinkedList:
    # @ for constructor
    def __init__(self):
        self.head = None

    # It adds the node with given data at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = new_node
        return

    def print(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    # It inserts data with given node at particular location

    def insertion(self, previous_node, data):
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    # Delete node with given data

    def deletion(self, data):
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            current_node = None
        return

        previous_node = None
        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = current_node.next
        current_node = None
        return

    # It reverses the linked list
    def reverse(self, data):
        current_node = self.head
        while current_node != None:
            if current_node == None:
                print(current_node.data)
                self.head = current_node.next
                current_node = None

        return

    # Count number nodes in linked list

    def traverse(self):
        count = 0
        current_node = self.head
        while current_node.next != None:
            count += 1
            current_node = current_node.next
        return count


ll = LinkedList()

prime_numbers = []
anagram = []
flag = 0
for number in range(0, 100):
    if number > 1:
        for iterating_number in range(2, number):
            if number % iterating_number == 0:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:

            if number not in prime_numbers:
                prime_numbers.append(str(number))
                ll.append(number)

# @ creating object
ll.print()
s1 = []
s2 = []
length = ll.traverse()
for iterating_number in range(length):
    for iterating_number1 in range(length):
        if len(prime_numbers[iterating_number]) == len(prime_numbers[iterating_number1]):
            if len(prime_numbers[iterating_number]) > 1:
                if len(prime_numbers[iterating_number1]) > 1:
                    queue_1 = (list(prime_numbers[iterating_number]))
                    queue_2 = (list(prime_numbers[iterating_number1]))
                    queue_1.sort()
                    queue_2.sort()
                    # print(queue_1)
                    if queue_1 == queue_2:
                        s1.append(prime_numbers[iterating_number])
                        s2.append(prime_numbers[iterating_number1])
                        # print(prime_numbers[iterating_number], " is anangram of ",

                        #       prime_numbers[iterating_number1])
while s1 != None:
    try:
        val1 = s1.pop()
        val2 = s2.pop()
        print(val1, " is anangram of ", val2)
    except IndexError:
        pass
