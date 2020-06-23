class Queue(object):
    def __init__(self,queue_size: int=10):
        self.arr = [0 for _ in range(queue_size)]
        self.front_index = -1
        self.next_index = 0
        self.queue_size = 0

'''

In the cell below, add the code for the enqueue method.

The method should:

Take a value as input and assign this value to the next free slot in the array
Increment queue_size
Increment next_index (this is where you'll need to use the modulo operator %)
If the front index is -1 (because the queue was empty), it should set the front index to 0
'''
class Queue2():
    def __init__(self,queue_size: int=10):
        self.arr = [0 for _ in range(queue_size)]
        self.front_index = -1
        self.next_index = 0
        self.queue_size = 0
    
    def enqueue(self, value):
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index +1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0


