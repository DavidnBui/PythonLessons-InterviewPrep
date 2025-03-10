class Node:                        # Building block for LinkedList
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)      # Creates Node 
        self.head = new_node        # Sets node as head 
        self.tail = new_node        # Sets node as tail
        self.length = 1             # Update length of node 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):           # Adds a node to the end of the list
        new_node = Node(value) 
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Adds new node to the end of list
            self.tail = new_node       # Sets the new note as the tail
        self.length += 1

    def pop(self):                      # Removes last node on the list 
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

    def prepend(self, value):           # Adds a node to the begining of the list
        new_node = Node(value)          
        if self.length == 0:
            self.head = new_node        
            self.tail = new_node       
        else:
            new_node.next = self.head   # Adds new node to the begining of list 
            self.head = new_node        # Sets the new node as the head
        self.length += 1
        return True

    def pop_first(self):                # Removes first node from the lsit 
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

    def set_value (self, index, value): # Goes to index of node and changes its value 
        temp = self.get(index)          # calls back to get method 
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value): 
        if index < 0 or index > self.length:
            return False
        if index == 0:                  # Inserts new node at the begining 
            return self.prepend(value)
        if index == self.length:        # Inserts new node at the end
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)      # Do -1 because you want the one before it so it can point to next
        new_node.next = temp.next       # Sets pointer to the node after the new node
        temp.next = new_node            # Points temp arrow to new node 
        self.length += 1 
        return True

    def remove (self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:                  # Removes item at the begining 
            return self.pop_first()
        if index == self.length - 1:    # Removes item as the end 
            return self.pop()
        prev = self.get(index - 1)      # Gets item before the one you want to remove
        temp = prev.next                # Item that needs to be removed 
        prev.next = temp.next           # assigns the next item to the item after the one you removed
        temp.next = None
        self.length -= 1 
        return temp

    def reverse (self):                 # VERY COMMON INTERVIEW QUESTION
        temp = self.head                # Line 111 --> Line 113 Reverses the head and tail
        self.head = self.tail 
        self.tail = temp
        after = temp.next              
        before = None
        for _ in range(self.length):
            after = temp.next           # Moves after varaible over one 
            temp.next = before          # Makes temp variable flip and point to the item before
            before = temp               # Moves before variable over one
            temp = after                # Moves temp variable behind one

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list()