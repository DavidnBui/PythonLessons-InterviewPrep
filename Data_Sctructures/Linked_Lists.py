class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value) 
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value) 
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Adds new node to the end of list
            self.tail = new_node       # Sets the new note as the tail
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):              # Iterates through the list as long as temp doesn't hit None
            pre = temp                 # Pre will now be the second to last node
            temp = temp.next           # Once temp hits none, It will now point towards the last node 
        self.tail = pre                # Sets the second to last node as the tail
        self.tail.next = None          # Removes the last node 
        self.length -= 1
        if self.tail == 0: 
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)          
        if self.length == 0:
            self.head = new_node        
            self.tail = new_node       
        else:
            new_node.next = self.head   # Adds new node to the begining of list 
            self.head = new_node        # Sets the new node as the head
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head                # Creates temporary Node 
        self.head = self.head.next      # Moves head of the Node to the next one
        temp.next = None                # Removes the previous head from the list
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range (index):         # Iterate however many times to reach index
            temp = temp.next            # Move temp along the list 
        return temp

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.prepend(1)
my_linked_list.print_list()