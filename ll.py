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
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        # to insert, we need a variable that points to the index before we are inserting
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node 
        self.length += 1 
        return True 
    #return None instead of False b/c if you're successful in insert, you return True 
        #in remove, if we're successful, we return a node 
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:  # last index 
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next 
        temp.next = None 
        self.length -= 1 
        return temp 

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
#[11, 3, 23, 7]
    #without using length 
    def find_middle_node(self):
        slow = self.head
        fast = self.head 
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next 
        return slow 
    
    def has_loop(self):
        slow = self.head
        fast = self.head 
        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_kth_from_end(ll, k):
        slow, fast = ll.head 
        for _ in range(k):
            if fast == None:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow 

    def reverse_between(self, m, n):
        if self.length <= 1:
            return 
        dummy = Node(0) #dummy handles cases when the head of the list is also reversed
        dummy.next = self.head 
        prev = dummy 
        #move the prev pointer forward 
        for i in range(m):
            prev = prev.next
        # after the loop, the prev will point to the node just before the mth node (m-1)
        current = prev.next 
        #iterate from 0 to n-m to reverse the section of the linked list between those indicies 
        for i in range(n - m):
            #temp = current.next (next node to be reversed)
            #the temp pointer holds the next node that will be moved to the beginning of the reversed section
            temp = current.next
            #detach temp from its current position and connect the current node to the remaing part of the sublist that is yet to be reversed
            current.next = temp.next
            #update temp.next to point to the node currently next to prev 
            #places temp node at beginning of reversed section
            temp.next = prev.next
            #connect temp node 
            prev.next = temp 
        #after each iteration, the current node remains the same but the sublist between the current node and the nth node is gradually reversed
        #update head to the node next to the dummy to ensure that if the head was reversed, the new head will be correctly assigned
        self.head = dummy.next

    #O(n) with set 
    def remove_duplicates(self):
        values = set()
        previous = None
        current = self.head 
        while current != None:
            if current.value in values:
                previous.next = current.next 
                self.length -= 1 
            else:
                values.add(current.value)
                previous = current
            current = current.next

        


        


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()


