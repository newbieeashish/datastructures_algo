'''
Goal will be to implement a Stack class that has the following behaviors:

push - adds an item to the top of the stack
pop - removes an item from the top of the stack (and returns the value of that item)
size - returns the size of the stack
top - returns the value of the item at the top of stack (without removing that item)
is_empty - returns True if the stack is empty and False otherwise

'''


class Stack:
    def __init__(self, intial_size = 10):
        self.arr = [0 for _ in range(intial_size)]
        self.next_index  =0
        self.num_element = 0
    '''Push Method'''
    def push(self, data):
        self.arr[self.next_index] = data
        self.next_index +=1
        self.num_element +=1

        '''above method will not handle capcity full error'''
    
    def new_push(self, data):
        if self.next_index == len(self.arr):
            print('out of space')
            self._handle_stack_capacity_full()
        
        self.arr[self.next_index] = data
        self.next_index +=1
        self.num_element +=1

    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2*len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

    

    




    







