from collections import Counter

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        print (counter[c])
        counter[c] += 1
        print (counter[c])
    for c in str2:
        if counter[c] == 0:
            return False
        print (counter[c])
        counter[c] -= 1
    return True

if check_permutation('abcd', 'cabbd'):
    print("same")
else:
    print("different")
