class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
head = Node(2)
head.next = Node(1)
print(head.value)

'''in above example we have created a simple linked list now we will see how to 
traverse through the linked list'''

def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(value)
    return head
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list(input_list)
test_function(input_list, head)


''' more efficient solution'''

def create_linked_list_new(input_list):
    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head

        else:
            tail.next = Node(value)
            tail = tail.next

    return head
def test_function1(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list_new(input_list)
test_function1(input_list, head)

input_list = [1]
head = create_linked_list_new(input_list)
test_function1(input_list, head)

input_list = []
head = create_linked_list_new(input_list)
test_function1(input_list, head)
