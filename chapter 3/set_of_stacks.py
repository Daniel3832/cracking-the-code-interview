import unittest

class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        
    def createNewStack(self):
        new_stk = Stack(self.capacity)
        self.stacks.append(new_stk)

    def push(self, val):
        if self.stacks and self.stacks[-1].size < self.capacity:
            self.stacks[-1].push(val)
        else:
            self.createNewStack()
            self.stacks[-1].push(val)

    def pop(self):
        if not self.stacks:
            return None
        else:
            val = self.stacks[-1].pop()
            if self.stacks[-1].size == 0:
                del self.stacks[-1]
        return val


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
    
    def isEmpty(self):
        if self.size == 0: 
            return True
        else:
            return False
    
    def push(self, val):
        top = Node(val)
        top.next = self.top
        self.top = top
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return None
        else:
            val = self.top.data
            self.top = self.top.next
            self.size -= 1
            return val

class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        self.assertEqual(lst, list(reversed(range(35))))

    # def test_pop_at(self):
    #     stacks = SetOfStacks(5)
    #     for i in range(35):
    #         stacks.push(i)
    #     lst = []
    #     for _ in range(31):
    #         lst.append(stacks.pop_at(0))
    #     self.assertEqual(lst, list(range(4, 35)))

if __name__ == '__main__':
    unittest.main()
        



