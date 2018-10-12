# stack solution

def isPermutation(string1, string2):

    if len(string1) != len(string2):
        print('not permutation')

    stack = []
    for char in list(string1): 
        stack.append(char)
    for char in list(string2):
        if char in stack:
            stack.remove(char)

    if len(stack) != 0:
        print('Not Permutation')
    else:
        print('permutation')

isPermutation('yao', 'oya')
