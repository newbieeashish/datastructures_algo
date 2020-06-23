'''singly linkedlist'''

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
'''creating small linkedlist'''

head = Node(1)
head.next = Node(2)

'''appending values'''

class linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        else:
            node = self.head
            while node.next:
                node = node.next
            
            node.next = Node(value)
            return

'''Note that if we're only tracking the head of the list, this runs in linear time -  𝑂(𝑁)
 since you have to iterate through the entire list to get to the tail node. '''

linked_list = linkedlist()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next

'''Add a method to_list to LinkedList that converts linked list back into python list'''

class LinkedListNew:
    def __init__(self):
        self.head = None
    
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            return

        else:
            node = self.head
            while node.next:
                node = node.next

            node.next = Node(value)
            return
    
    def to_list(self):
        new_list = []
        node = self.head
        while node:
            new_list.append(node.value)
            node = node.next
        return new_list
    
linked_list = LinkedListNew()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")

'''doubly linked list'''

class DoubleNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        else:
            self.tail.next = DoubleNode(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
            return

linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous