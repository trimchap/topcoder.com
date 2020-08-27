# Linked List Node
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value
        
    def get_next(self):
        return(self.next)
    
    def set_next(self, new_next):
        self.next = new_next
    
def populate_linked_list(values):
    if values == []:
        head = None
        return
    head = Node(values[0])
    for value in values[1:]:
        new_node = Node(value)
        new_node.next = head
        head = new_node
    return head

def print_linked_list(head):
    print_node = head
    while print_node:
        print(print_node.value)
        print_node = print_node.next

def reverse_linked_list(head):
    # if linked list is empty, return
    if not head:
        return(head)
    # set previous and next pointers
    prev = None
    curr = head.next
    # until the end of the list, reverse
    while curr:
        head.next = prev
        prev = head
        head = curr
        curr = curr.next
    # connect the last node before returning
    head.next = prev

    return head


#------------------
# Test Linked List
#------------------
values = ['d','c','b','a']
# values = []
# values = [3,2,1]
head = populate_linked_list(values)
print_linked_list(head)
head = reverse_linked_list(head)
print("reversed:")
print_linked_list(head)