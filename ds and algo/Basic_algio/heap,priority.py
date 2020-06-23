'''

Priority Queues - Intuition
Consider the following scenario -

A doctor is working in an emergency wing at a hospital. When patients come in,
 a nurse checks their symptoms and based on the severity of the illness, sends
  them to the doctor. For e.g. a guy who has had an accident is sent before 
  someone who has come with a runny nose. But there is a slight problem. There 
  is only one nurse and only one doctor. In the amount of time nurse takes to 
  check the symptoms, the doctor has to work alone with the patients, hurting 
  their overall productivity.

You are a ninja programmer. The doctor comes to you for help. Your job is to 
write a small software in which patients will enter their symptoms and will 
receive a priority number based on their illness. The doctor has given you a 
list of common ailments, and the priority in which he would prefer seeing them. 
How would you solve the priority problem?
'''

'''Priority Queues
Like the name suggests, a priority queue is similar to a regular queue, except 
that each element in the queue has a priority associated with it. A regular queue 
is a FIFO data structure, meaning that the first element to be added to the queue
lso the first to be removed.

With a priority queue, this order of removal is instead based on the priority.
 Depending on how we choose to set up the priority queue, we either remove the 
 element with the most priority, or an element of the least priority.

For the sake of discussion, let's focus on removing the element of least priority
or now.'''



#How should we implement it?

'''
Arrays
Earlier, we saw that one way to implement a queue was by using an array. We could do a similar thing for priority queues. 
We could use the array to store our data.

Insertion in an array is very fast. Unless the array is full, we can do it in O(1) time.

Note: When the array is full, we will simply create a new array and copy all the elements from our old array to new array. 
It's exactly similar to what we do for our queue's implementation using arrays.

What about removal? We always want to remove the smallest or highest priority data from the array, depending on if 
this is a max-heap or min-heap. In the worst case, we will have to search the entire array, which will take O(n) time. 
Thus, to remove the element, the time complexity would be O(n).

This also creates an additional problem for us. The index from which we removed the element is now empty. We cannot leave empty 
indices in our array. Over the course of operations, we will be wasting a lot of space if we did that.

Therefore, insertion no longer happens in O(1) time. Rather, every time we insert, we will have to look for these empty indices
 and put our new element in the first empty index we find. In the worst case, this also takes O(n) time. 
 Therefore, our time complexity with arrays (for both insertion and removal) would be O(n).'''



#LinkedList

'''
LinkedList
Insertion is very easy in a linked list. If we maintain a variable to keep track 
of the tail of the linked list, then we can simply add a new node at this
 location. Thus, insertion takes O(1) time.

For removal, we will have to traverse the entire list and find the smallest 
element, which will require O(n) time.

Note that with linked lists, unlike arrays, we do not have to worry about empty 
indices.

A linked linked certainly seems to be a better option than an array. Although 
they have the same time complexity for removal, the time complexity for insertion 
better.'''


#HashMap


'''HashMap
The same problem lies in HashMap as well. We can insert in O(1) time. 
Although, we can remove an element from a HashMap in O(1) time but we have to 
first search for the smallest element in the map. This will again take O(n) time. 
efore, the time complexity of remove is O(n) for hashmaps.'''



#BST

'''Binary Search Trees
Binary Search Trees are laid out according to the value of the node that we want
 to insert. All elements greater than the root go to the right of the root, and 
 all elements smaller than the root go to the left of the root.

If we assume that our Binary Search tree is balanced, insertion would require 
O(h) time in the worst case. Similarly, removal would also require O(h) time.
 Here h is the height of the binary search tree.'''



#HEAP

'''Heaps
A heap is a data structure with the following two main properties:

Complete Binary Tree
Heap Order Property
Complete Binary Tree - Like the name suggests we use a binary tree to create 
heaps. A complete binary tree is a special type of binary tree in which all 
levels must be filled except for the last level. Moreover, in the last level, 
the elements must be filled from left to right.'''


'''Heap Order Property - Heaps come in two flavors
Min Heap
Max Heap
Min Heap - In the case of min heaps, for each node, the parent node must be 
smaller than both the child nodes. It's okay even if one or both of the child 
nodes do not exists. However if they do exist, the value of the parent node 
must be smaller. Also note that it does not matter if the left node is greater
 than the right node or vice versa. The only important condition is that the 
 root node must be smaller than both it's child nodes
Max Heap - For max heaps, this condition is exactly reversed. For each node, 
the value of the parent node must be larger than both the child nodes.
Thus, for a data structure to be called a Heap, it must satisfy both of the
 above properties.

It must be a complete binary tree
It must satisfy the heap order property. If it's a min heap, it must satisfy 
the heap order property for min heaps. If it's a max heap, it should satisfy 
the heap order property for max heaps.'''



class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index 

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            # compare with right child
            if right_child is not None:
                min_element = min(right_child, min_element)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]



heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))
    
print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))
