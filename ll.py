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
            self.tail.next = new_node
            self.tail = new_node 
        self.length += 1 
        return True # optional 
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head = new_node 
        self.length += 1 
        return True 

    def insert(self, index, value):
        pass

    def pop(self):
        if self.length == 0:
            return None 
        temp = self.head 
        prev = self.head
        while (temp.next): #while it's pointing to a node aka not the end 
            prev = temp 
            temp = temp.next # to move it to the next 
        self.tail = prev 
        self.tail.next = None 
        self.length -= 1 
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp # or temp.value 
    
    def pop_first(self):
        if self.length == 0:
            return None 
        temp = self.head 
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp 
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head 
        for _ in range(index): # if it's an index of 2, it will range from 0 - 2 
            temp = temp.next 
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value 
            return True 
        return False 


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()


