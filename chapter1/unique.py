# is unique return true, else false
# abb
# check chars in a string is unique or not.
# [F, F, F, F....] as long as the string length: char_set[]
# get the char in the string. 
# return the ASCII code of this char and store it in val
# check if char_set[val] is true   

def isUnique(str):
    if len(str)>128:
        return False

    char_set = [False for _ in range(128)]
    for char in str:
        val = ord(char)                
        if char_set[val]:
            return False
        char_set[val] = True

    return True

if isUnique("hello"):
    print ("not unique")
print ("unique")

print(ord('a'))