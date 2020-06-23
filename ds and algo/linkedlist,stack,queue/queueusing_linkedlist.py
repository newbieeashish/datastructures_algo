class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
    
class Queue():
    def __init__(self):
        self.tail = None
        self.head = None
        self.num_elements = 0

    
    def enqueue(self,value):
        new_node = Node(value)
        if self.num_elements == 0:
            self.head = new_node
            self.tail = self.head
        
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        
        self.num_elements +=1
    
