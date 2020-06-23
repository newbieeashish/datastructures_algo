
'''implement a function that detects if a loop exists in a linked list.
The way we'll do this is by having two pointers, called "runners",
moving through the list at different rates. Typically we have a "slow" runner
which moves at one node per step
and a "fast" runner that moves at two nodes per step.

If a loop exists in the list,
 the fast runner will eventually move behind the slow runner as
  it moves to the beginning of the loop.
  Eventually it will catch up to the slow runner and both runners will be
  pointing to the same node at the same time.
  If this happens then you know there is a loop in the linked list. '''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, init_list = None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

list_with_loop = LinkedList([2,-1,3,0,5])

#creating a loop where the last node points back to second node

loop_start = list_with_loop.head.next
node = list_with_loop.head
while node.next:
    node = node.next

node.next = loop_start

'''Given a linked list, implement a function iscircular that 
returns True if a loop exists in the list and False otherwise.'''

def isCircular(linked_list):
    if linked_list.head is None:
        return False
    
    slow_runner = linked_list.head
    fast_runner = linked_list.head

    while fast_runner and fast_runner.next:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
        if slow_runner == fast_runner:
            return True

    return False


# Test Cases

small_loop = LinkedList([0])
small_loop.head.next = small_loop.head
print ("Pass" if isCircular(list_with_loop) else "Fail")
print ("Pass" if not isCircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
print ("Pass" if not isCircular(LinkedList([1])) else "Fail")
print ("Pass" if isCircular(small_loop) else "Fail")
print ("Pass" if not isCircular(LinkedList([])) else "Fail")






    
