def isUnique(string):
    my_list = list(string)

    appeared_Char = []
    
    for element in my_list:
        if element in appeared_Char:
            print('not unique')
            return False
        else:
            appeared_Char.append(element)
    
    print ('is unique')
    return True


string = 'abcde'

isUnique(string)

