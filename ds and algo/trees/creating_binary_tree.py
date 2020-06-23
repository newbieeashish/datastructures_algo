#defining Node

class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
    
    def get_value(self):
        return self.value
    
    def set_value(self,value):
        self.value = value
    
    def set_left_child(self,node):
        self.left = node
    
    def set_right_child(self, node):
        set.right = node
    
    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    
class Tree(object):
    def __init__(self, node = None):
        self.root = node
    
    def get_root(self):
        return self.root
    
    
