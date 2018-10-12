import unittest

class MyQueue:
    def __init__(self):
        self.front = None
        self.end = None
        self.stk1 = []
        self.stk2 = []

    # push to stk1
    def push(self, val):
        if not self.stk1 and not self.stk2:
            self.stk1.append(val)
        elif self.stk1:
            self.stk1.append(val)
        else:
            self.stk2.append(val)

    def pop(self):
        if not self.stk1 and not self.stk2:
            return None
        elif self.stk1:
            while len(self.stk1) > 1:
                self.stk2.append(self.stk1.pop())
            val = self.stk1.pop()
        else:
            val = self.stk2.pop()
        return val

class Test_Queue(unittest.TestCase):
    def test_queue(self):
        q = MyQueue()
        for i in range(10):
            q.push(i)
        lst = []
        for _ in range(10):
            lst.append(q.pop())
        self.assertEqual(lst, list(range(10)))

if __name__ == "__main__":
    unittest.main()