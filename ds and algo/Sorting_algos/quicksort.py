'''

QuickSort
Like MergeSort, QuickSort is a divide-and-conquer algorithm. 
We need to pick a pivot, then sort both sublists that are created 
on either side of the pivot. '''

items = [8, 3, 1, 7, 0, 10, 2]

pivot_index = len(items) -1
pivot_value = items[pivot_index]


'''Because we plan on sorting in-place, we want to iterate through
 the items to the left of our pivot (left_items). When they're 
 larger than pivot_value though, we will not increment our position 
 through left_items, but instead change pivot_index. We'll know
  we're done with this pass when pivot_index and left_items index 
  are equal.'''

left_index = 0
while (pivot_index!=left_index):
    item = items[left_index]

    if item <=pivot_value:
        left_index +=1
        continue

    #place the item befor the pivot at left index
    items[left_index] = items[pivot_index - 1]

    #shift pivot one to the left

    items[pivot_index-1] = pivot_value

    #place item at pivot previous location

    items[pivot_index] = item

    #update pivot_index

    pivot_index -=1

print(items)


'''When our loop terminated, we knew everything to the left of our
 pivot was less than pivot, and everything to the right of our pivot
 greater than pivot. Great! Now we need to do that again for the
  sublists that are left and right of pivot's final location.

We can do that by abstracting our above code to a function, just 
passing the list of items as a parameter.'''


def sort_a_little_bit(items):
    left_index = 0 
    pivot_index = len(items) -1
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):
        left_index += 1
        continue

    items[left_index] = items[pivot_index-1]
    items[pivot_index - 1] = pivot_value
    items[pivot_index] = item
    pivot_index -=1

items = [8, 3, 1, 7, 0, 10, 2]
sort_a_little_bit(items)
print(items)

'''
Now what would it require to recurse on this? 
We want to take the result of that iteration and act on it. So first
f, we see that in order to call the function again, we need to 
communicate the final pivot_index value. And then with that, we can
 mark off segments of the list and have our function operate on less
 an the entire list. So let's change our function to accept the 
 indices it should stay within, and return the pivot_index.'''


def sort_a_little_bit1(items, begin_index, end_index):    
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1
    
    return pivot_index

items = [8, 3, 1, 7, 0, 10, 2]
pivot_index = sort_a_little_bit1(items, 0, len(items) - 1)
print(items)
print('pivot index %d' % pivot_index)


'''
Almost there! Let's create another function, the recursive function
 we want, that uses this. And then we'll have our top level
  definition of quicksort call it with our initial parameters. 
  But we need a way to know if we're done! We'll use the indices 
  to see if they demark a list of more than one item. If the 
  demarked sublist is 0 or 1 item, we know it's already sorted.'''

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort_a_little_bit1(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    
def quicksort(items):
    sort_all(items, 0, len(items) - 1)
    
items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)


items = [1, 0]
quicksort(items)
print(items)

items = [96, 97, 98]
quicksort(items)
print(items)