#  Create a linked list  - linear DS similar to arrays
#  linear data struct containing data and reference to next element

# Assuming data stored in node is int - 4 bytes
# reference next pointer 
#   - incase of 32 bit system - 4 bytes. So total 8 bytes for a node
#   - incase of 64 bit system - 8 bytes. So total 12 bytes for a node
  
# Stacks and queues are built on top of linked list
# Dynamic memory allocation is made feasible by linked list to manage and allocate memory blocks efficiently
# Application example: Webbrowsers

# Types: 
#   - Singly linked
#   - Doubly linked 
#   - circular
#   - Sorted

class Node:
    def __init__(self,val:int):
        self.data = val
        self.next = None
        
# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Method to insert node at beginning   
    def insert_at_begin(self, val:int):
        new_node:Node = Node(val)
        # also handle case where linkedlist is empty, implying head is pointing to null
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to insert node at any index [0, anything]
    def insert_at_index(self, val:int, index:int):
        if index == 0:
            self.insert_at_begin(val)
        curr_node:Node = self.head
        position = 0
        # Traverse the linkedlist till you find position == index-1
        while(curr_node.next!=None and position != index-1):
            position+=1
            curr_node = curr_node.next
        # Now insert at this position, 
        # unless you reached null pointer which in this case means index was too big and you already traversed the entire list
        if(curr_node!=None):
            # insert at this position
            new_node:Node = Node(val)
            new_node.next = curr_node.next
            curr_node.next = new_node
        else:
            print("Invalid index")

    # Method to insert at end       
    def insert_at_end(self,val:int):
        new_node:Node = Node(val)
        if self.head is None:
            self.head = new_node
        curr_node:Node = self.head
        while(curr_node.next):
            curr_node = curr_node.next
        curr_node.next = new_node
        
    # Update node of a linked list
    # at given position
    def updateNode(self, val:int, index:int):
        if index == 0:
            self.head.data = val
            return
        position = 0
        curr_node = self.head
        while(curr_node.next!=None and position!= index):
            position+=1
            curr_node = curr_node.next
        if(curr_node!=None):
            curr_node.data = val
        else:
            print("invalud index")
    
    # Method to remove first node 
    def remove_first_node(self):
        if not self.head:
            return
        self.head = self.head.next
       
    # Method to remove last node 
    def remove_last_node(self):
        if self.head is None or self.head.next is None:
            return
        curr_node = self.head
        while(curr_node.next!=None and curr_node.next.next!=None):
            curr_node = curr_node.next
        if curr_node.next == None:
            self.head = None
        else:
            curr_node.next = None
     
    # Method to remove node containing data 
    # Assumption: at most one node contains this data       
    def remove_node(self, data):
        if self.head.data == data:
            self.remove_first_node()
            return 
        curr_node = self.head
        while(curr_node.next!=None and curr_node.next.data != data):
            curr_node = curr_node.next
        if not curr_node:
            return     
        curr_node.next = curr_node.next.next
        
    # Method to remove node at given index
    def remove_at_index(self, index):
        if index == 0:
            self.head = None
            return
        position = 0
        curr_node:Node = self.head
        while(curr_node.next!=None and position!= index-1):
            position+=1
            curr_node = curr_node.next
        if curr_node is not None:
            curr_node.next = curr_node.next.next
        else:
            print("Invalid index")
            
    def sizeOfLL(self) -> int:
        size_ll:int = 0
        if (self.head):
            curr_node:Node = self.head
            while(curr_node):
                size_ll+=1
                curr_node = curr_node.next
        return size_ll
