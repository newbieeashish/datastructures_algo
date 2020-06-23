
# depth first search

'''Traversing a tree means "visiting" all the nodes in the tree once. 
Unlike an array or linked list, there's more than one way to walk through a tree,
 starting from the root node.

Traversing a tree is helpful for printing out all the values stored in the tree,
 as well as searching for a value in a tree, inserting into or deleting values 
 from the tree. There's depth first search and breadth first search.

Depth first search has 3 types: pre-order, in-order, and post-order.
for more details https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/



'''

# this code makes the tree that we'll traverse

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root


# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


# defining a stack to help keep track of the tree node

class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"


# check Stack
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
print(stack.pop())
print("\n")
print(stack) 


visit_order = list()
stack = Stack()

# start at the root node, visit it and then add it to the stack
node = tree.get_root()
stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")


# visit apple
visit_order.append(node.get_value())
print(f"""visit order {visit_order}
{stack}
""")


# check if apple has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since apple has a left child (banana)
# we'll visit banana and add it to the stack
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")


# visit banana
print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order {visit_order}""")



# check if banana has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since banana has a left child "dates"
# we'll visit "dates" and add it to the stack
if node.has_left_child():
    node = node.get_left_child()    
    stack.push(node)
    
print(f"""
visit_order {visit_order} 
stack:
{stack}
""")


# visit dates
visit_order.append(node.get_value())
print(f"visit order {visit_order}")


# check if "dates" has a left child
print(f"{node} has left child? {node.has_left_child()}")




# since dates doesn't have a left child, we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")



# since "dates" is a leaf node (has no children), we can start to retrace our steps
# in other words, we can pop it off the stack.
print(stack.pop())



print(stack)


# now we'll set the node to the new top of the stack, which is banana
node = stack.top()
print(node)



# we already checked for banana's left child, so we'll check for its right child
print(f"{node} has right child? {node.has_right_child()}")


# banana doesn't have a right child, so we're also done tracking it.
# so we can pop banana off the stack
print(f"pop {stack.pop()} off stack")
print(f"""
stack
{stack}
""")


# now we'll track the new top of the stack, which is apple
node = stack.top()
print(node)


# we've already checked if apple has a left child; we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")


# since it has a right child (cherry), 
# we'll visit cherry and add it to the stack.
if node.has_right_child():
    node = node.get_right_child()
    stack.push(node)
    
print(f"""
visit_order {visit_order} 
stack
{stack}
""")


# visit cherry
print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order: {visit_order}""")



# Now we'll check if cherry has a left child
print(f"{node} has left child? {node.has_left_child()}")

# it doesn't, so we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")


# since cherry has neither left nor right child nodes,
# we are done tracking it, and can pop it off the stack

print(f"pop {stack.pop()} off the stack")

print(f"""
visit_order {visit_order} 
stack
{stack}
""")


# now we're back to apple at the top of the stack.
# since we've already checked apple's left and right child nodes,
# we can pop apple off the stack

print(f"pop {stack.pop()} off stack")
print(f"pre-order traversal visited nodes in this order: {visit_order}")


print(f"""stack
{stack}""")











class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def get_visited_left(self):
        return self.visited_left
    
    def get_visited_right(self):
        return self.visited_right
    
    def set_visited_left(self):
        self.visited_left = True
        
    def set_visited_right(self):
        self.visited_right = True
        
    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s







def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while(node):
        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
        count +=1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None
            
    if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
    return visit_order



# check pre-order traversal

pre_order_with_stack(tree, debug_mode=True)


'''pre_order recursion'''

def pre_order(tree: Tree):
    return pre_order_dfs(tree.get_root())


def pre_order_dfs(node: Node):

    if (not node.has_left_child()) and (not node.has_right_child()):  # We reached a leaf
        return [node.get_value()]

    lvl_visited = [node.get_value()]  # First time we visit the node, it is saved

    if node.has_left_child():
        lvl_visited.extend(pre_order_dfs(node.get_left_child()))

    if node.has_right_child():
        lvl_visited.extend(pre_order_dfs(node.get_right_child()))

    return lvl_visited

pre_order(tree)


'''in order'''


# define in-order traversal
def in_order(tree: Tree):
    """
    Traverse the left subtree, then visit the node, and then traverse the right subtree.
    """
    return in_order_dfs(tree.get_root())


def in_order_dfs(node: Node):

    if (not node.has_left_child()) and (not node.has_right_child()):  # We reached a leaf
        return [node.get_value()]

    lvl_visited = []

    if node.has_left_child():
        lvl_visited.extend(in_order_dfs(node.get_left_child()))  # Traverse left node

    lvl_visited.extend([node.get_value()])  # First time we visit the node, it is saved

    if node.has_right_child():
        lvl_visited.extend(in_order_dfs(node.get_right_child()))  # Traverse right node

    return lvl_visited


in_order(tree)

'''post order'''

# define post_order traversal
def post_order(tree: Tree):
    """
    Traverse left subtree, then right subtree, and then visit the node.
    """
    return post_order_dfs(tree.get_root())


def post_order_dfs(node: Node):

    if (not node.has_left_child()) and (not node.has_right_child()):  # We reached a leaf
        return [node.get_value()]

    lvl_visited = []

    if node.has_left_child():
        lvl_visited.extend(post_order_dfs(node.get_left_child()))  # Traverse left node

    if node.has_right_child():
        lvl_visited.extend(post_order_dfs(node.get_right_child()))  # Traverse right node
    
    lvl_visited.extend([node.get_value()])  # First time we visit the node, it is saved

    return lvl_visited


    
# check solution: should get: ['dates', 'banana', 'cherry', 'apple']
post_order(tree)









