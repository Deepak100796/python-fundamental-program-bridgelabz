"""
creating queue class
"""
"""


    @date   : 1/11/2019
    @Author: DeepakMishra
    @guide by: Gunjan sharma
"""

# @queue class
class Queue:
    def __init__(self):
        self.items = []

    # @creating empty or not
    def is_empty(self):
        return self.items == []

    # @for add
    def enqueue(self, data):
        self.items.append(data)

# @ for delete
    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def get_queue(self):
        return self.items

"""
driver code
"""
queue = Queue()
# if __name__ == '__main__':
#     # creating object of queue
#     q = Queue()
#     while True:
#         print('enqueue <value>')
#         print('dequeue')
#         print('quit')
#         print("size")
#         print("print")
#         do = input('What would you like to do? ').split()
#
#         operation = do[0].strip().lower()
#         if operation == 'enqueue':
#             q.enqueue(int(do[1]))
#         elif operation == 'dequeue':
#             if q.is_empty():
#                 print('Queue is empty.')
#             else:
#                 print('Dequeued value: ', q.dequeue())
#         elif operation == 'print':
#             print(q.get_queue())
#         elif operation == "size":
#             print(q.size())
#         elif operation == 'quit':
#             break