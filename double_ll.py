class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
        self.prev = None 

class DoublyLinkedList:
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
             new_node.prev = self.tail 
             self.tail = new_node 
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
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head 
        if index < self.length//2:
            for _ in range(index):
                temp = temp.next 
        else:
            temp = self.tail 
            for _ in range(self.length - 1, index, -1): # go backwards
                temp = temp.prev
        return temp 
    
    def set(self, index, value):
        temp = self.get(index)
        if temp != None:
            temp.value = value 
            return True 
        return False 
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next 
        new_node.prev = before 
        before.next = new_node
        after.prev = new_node
        self.length += 1 
        return True 
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None 
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev 
        temp.prev.next = temp.next 

#swap first and last node 
    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return 
        self.head.value, self.tail.value = self.tail.value, self.head.value




def reverse(self):
        temp = self.head 
        self.head = self.tail
        self.tail = temp 
        after = temp.next
        before = None 
        for _ in range(self.length):
            # temp is 3 
            # after becomes 23 
            after = temp.next
            # now 3 points to before
            temp.next = before 
            #becomes 3 
            before = temp 
            #temp becomes 23
            temp = after 

#palindrome checker 
def is_palindrome(self):
    if self.length <= 1:
        return True 
    forward = self.head 
    backward = self.tail 
    for i in range(self.length // 2):
        if forward.value != backward.value:
            return False 
        forward = forward.next 
        backward = backward.prev 
    return True 

#swap nodes in pairs 
def swap_pairs(self):
    dummy = Node(0)
    dummy.next = self.head 
    prev = dummy 
    while self.head and self.head.next:
        first_node = self.head 
        second_node = self.head.next 
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node 
        second_node.prev = prev 
        first_node.prev = second_node 
        if first_node.next:
            first_node.next.prev = first_node 
        self.head = first_node.next
        prev = first_node 
    self.head = dummy.next
    if self.head:
        self.head.prev = None 


my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.print_list()
