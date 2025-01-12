class Node:                        
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__ (self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp= temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node       # Point to new node 
            new_node.prev = self.tail       # Points new node back 
            self.tail = new_node            # Set the new node as the tail
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail 
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev 
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node
        else: 
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None 
            temp.next = None 
        self.length -= 1 
        return temp

my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(1)

print(my_doubly_linked_list.print_list())
print(my_doubly_linked_list.print_list())
print(my_doubly_linked_list.print_list())
