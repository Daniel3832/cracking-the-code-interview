import unittest

# check if the characters in an string is unique
def isUnique(string):
    if len(string)>128:
        return False
    
    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if (char_set[val]):
            return False
        else:
            char_set[val] = True

    return True




text = raw_input("please enter a string: ")    

if(isUnique(text)):
    print ("is unique")
else:
    print("not unique")
