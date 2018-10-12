# 3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# thrshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there werejust a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs apopoperationon aspecificsub-stack.
# Hints:#64, #87

import unittest

class stackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    
    def __init__(self, capacity):
        self.top = None         #top stackNode
        self.capacity = capacity
        self.size = 0

    def isEmtpy(self):
        if self.top == None: return True
        else: return False
    
    def push(self, val):
        new_node = stackNode(val)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top == None:
            return None
        else:
            val = self.top.data
            self.top = self.top.next
            self.size -= 1
            return val
        

class SetOfStacks:

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def getLastStack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]

    def push(self, val):
        stk = self.getLastStack()
        if stk and stk.size < self.capacity:
            stk.push(val)
        else:
            new_stack = Stack(self.capacity)
            new_stack.push(val)
            self.stacks.append(new_stack)

    def pop(self):
        stk = self.getLastStack()
        if not stk:
            return None
        val = stk.pop()
        if stk.size == 0:
            del self.stacks[-1]
        return val
        # if not stk.isEmtpy():
        #     return stk.pop()
        # else:
        #     del self.stacks[-1]
        #     return None

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