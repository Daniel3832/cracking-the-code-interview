from linkedlist import LinkedList

def remove_dups(l):
    if not l:
        return

    current = l.head
    seen = set()
    seen.add(current.value)
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return l


ll = LinkedList()
ll.generate(9, 0, 9)
print(ll)
remove_dups(ll)
print(ll)

    
            


    

