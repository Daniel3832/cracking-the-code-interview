def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    newStr1 = ''.join(sorted(str1))
    newStr2 = ''.join(sorted(str2))

    if newStr1 == newStr2:
        return True
    else:
        return False

if isPermutation('yao', 'oya'):
    print("same")
else:
    print("different")
