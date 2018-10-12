import unittest

def pal_perm(s):
    check = {} 
    count = {}
    
    for c in s:
        count[c] = 0

    for c in s:
        if c not in check.keys():
            check[c] = True

    for c in s:
        check[c] = not check[c]
    
    return all(val == True for val in check.values()) and 

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
