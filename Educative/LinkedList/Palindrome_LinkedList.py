class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    slow = head
    fast = head
    tail = None
    count = 1
    middle = None 

    while(fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
        count += 2
    
    if fast.next:
        count+=1
        fast = fast.next
    
    tail = fast
    middle = slow

    reverse_the_list(slow)

    first = head
    last = tail
    i=0
    count = int(count/2)
    while(i<count):
        if first.value != last.value:
            return False
        first = first.next
        last = last.next
        i = i + 1
    return True

    return count

def reverse_the_list(head):
    # display(head)
    prev = head
    cur = head.next 
    temp = None
    while(cur):
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        

    # head.next = None
    return prev




def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()







