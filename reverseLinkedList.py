# Linked List Node
class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next_node = None

        
    def get_value(self):
        return self.value
        
    def get_next(self):
        return(self.next_node)
    
    def set_next(self, new_next):
        self.next_node = new_next
    

#------------------
# Test Linked List
#------------------
values = [5,14,77,100,9000]
# values = [3,2,1]

# populate a linked list with values
forward = []
backward = []
head = LinkedListNode(values[0])
forward.append(head.value)
for value in values[1:]:
    new_node = LinkedListNode(value)
    new_node.next_node = head
    head = new_node

print('list:')
print_node = head
while print_node:
    print(print_node.value)
    print(print_node.next_node)
    print_node = print_node.next_node


print('reversed:')

current_node = head
previous_node = None
next_node = None
print("head: ",current_node.value)
print(current_node.next_node)
#until we fall off the end of the list
while current_node != None:
    #copy the next pointer before overwriting
    next_node = current_node.next_node
    # reverse the 'next' pointer
    current_node.next_node = previous_node
    # step forward in the list
    previous_node = current_node
    current_node = next_node
    if current_node:
        print("newhead :",current_node.value)
        print(current_node.next_node)





