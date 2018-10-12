import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# FIFO
class Queue:
    def __init__(self):
        self.front = None
        self.end = None
    
    def isEmpty(self):
        if self.front == None:
            return True
        else: 
            return False
    
    def push(self, val):
        new_node = Node(val)
        if self.isEmpty():
            self.end = self.front = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def pop(self):
        if self.isEmpty():
            return None
        else:
            val = self.front.data
            self.front = self.front.next
            return val

class Tests(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        for i in range(35):
            q.push(i)
        lst = []
        for _ in range(35):
            lst.append(q.pop())
        self.assertEqual(lst, list(range(35)))


if __name__ == '__main__':
    unittest.main()