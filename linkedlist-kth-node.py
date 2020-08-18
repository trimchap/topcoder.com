class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def kth_to_last_node(k, head):
    current = head
    k_from_current = head
    distance = 0
    k_is_setup = False

    # step through list to the end
    while current:
        current = current.next
        # set up pointer at k back from current
        if k_is_setup == False:
            distance += 1
            if distance >= k:
                k_is_setup = True
        else:
            # wait until we are k away from current then start incrementing
            k_from_current = k_from_current.next
    if k_is_setup:
        return k_from_current
    else:
        return None



a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# Returns the node with value "Devil's Food" (the 2nd to last node)
kth_to_last_node(2, a)


