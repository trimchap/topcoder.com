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


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = LinkedListNode(value)
        new_node.set_next(self.head)
        self.head = new_node

    # big O = O(n) bc it has to visit every node
    def size(self):
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.get_next()
        return count

    # big O = O(n) bc it has to visit every node
    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.get_next()
        return

    # big O = O(n) bc - worst case - it has to visit every node
    def search(self, value):
        current = self.head
        while current:
            if current.get_value() == value:
                return current # found
            current.get_next()
        raise ValueError("value not in the list")
        return current

    # big O = O(n) bc - worst case - it has to visit every node  
    def delete(self, value):
        current = self.head
        found = False
        if current.get_value() == value:
            # found - delete the head node by assigning the next node as the new head
            self.head = current.get_next()
            found = True
        else:
            while current:
                previous_node = current
                current = current.next_node()
                if current.get_value() == value:
                    # found - now delete current by pointing previous to next
                    previous_node.set_next(current.get_next())
                    found = True
        if found == False:
            raise ValueError('value not in list')
        return


# Test Linked List
values = [5,14,77,100,9000]
linked_list = LinkedList()
for value in values[1:]:
    linked_list.insert(value)
print('list:')
linked_list.print()







