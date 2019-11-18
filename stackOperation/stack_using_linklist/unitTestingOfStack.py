import unittest

from dataStructureProgram.stackOperation.stack_using_linklist.stackMethods import LinkedList
class LinkedListTester(unittest.TestCase):

    def test_LinkedList_init(self):
        stack = LinkedList()
        self.assertEqual(0, stack.getSize())

    def test_push1_size(self):
        item = 5
        stack = LinkedList()
        stack.push(item)
        self.assertEqual(1, stack.getSize())

    def test_push1_items(self):
        stack = LinkedList()
        stack.push(5)
        self.assertEqual([5], stack.items)

    def test_push2_size(self):
        stack = LinkedList()
        stack.push(5)
        stack.push(6)
        self.assertEqual(2, stack.getSize())





    def test_push2_pop1_value(self):
        stack = LinkedList()
        stack.push(8)
        stack.push(9)
        self.assertEqual(9, stack.pop())

    def test_push2_pop2_size(self):
        stack = LinkedList()
        stack.push("Glob")
        stack.push("Blob")
        stack.pop()
        stack.pop()
        self.assertEqual(0, stack.getSize())


    def test_isEmpty_init(self):
        stack = LinkedList()
        self.assertEqual(True, stack.getSize())

    def test_isEmpty_push1(self):
        stack = LinkedList()
        stack.push(5)
        self.assertEqual(False, stack.getSize())

    def test_isEmpty_push1_pop1(self):
        stack = LinkedList()
        stack.push(1)
        stack.pop()
        self.assertEqual(True, stack.getSize())

    def test_peek_push1(self):
        stack = LinkedList()
        stack.push(88)
        self.assertEqual(88, stack.getSize())

    def test_peek_push3_pop1(self):
        stack = LinkedList()
        stack.push(7)
        stack.push(889)
        stack.push(3)
        stack.pop()
        self.assertEqual(889, stack.getSize())

    def test_pop_empty(self):
        stack = LinkedList()
        self.assertRaises(IndexError, stack.pop)

    def test_peek_empty(self):
        stack = LinkedList()
        self.assertRaises(IndexError, stack.getSize)

if __name__ == '__main__':
    unittest.main()
