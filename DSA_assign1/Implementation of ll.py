class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def append(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def insert(self, index, val):
        if index == 0:
            self.prepend(val)
            return
        new_node = Node(val)
        curr = self.head
        count = 0
        while curr and count < index - 1:
            curr = curr.next
            count += 1
        if curr:
            new_node.next = curr.next
            curr.next = new_node
    
    def delete(self, index):
        if self.is_empty():
            return
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        count = 0
        while curr and count < index - 1:
            curr = curr.next
            count += 1
        if curr and curr.next:
            curr.next = curr.next.next
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    
    def merge(self, other_list):
        if self.is_empty():
            self.head = other_list.head
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = other_list.head
    
    def interleave(self, other_list):
        curr1 = self.head
        curr2 = other_list.head
        while curr1 and curr2:
            next1 = curr1.next
            next2 = curr2.next
            curr1.next = curr2
            if next1 is None:
                break
            curr2.next = next1
            curr1 = next1
            curr2 = next2
    
    def middle_element(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val if slow else None
    
    def index_of(self, val):
        curr = self.head
        index = 0
        while curr:
            if curr.val == val:
                return index
            curr= curr.next
            index += 1
        return -1
    
    

