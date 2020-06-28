'''Given two binary trees and imagine that when you put one of 
them to cover the other, some nodes of the two trees are overlapped

 while the others are not.

You need to merge them into a new binary tree. The merge 
rule is that if two nodes overlap, then sum node values up as 
the new value of the merged node. Otherwise, the NOT null node 
will be used as the node of new tree.'''


# Definition for a binary tree node.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def MergeTree(self,t1,t2):
        if t1 is not None and t2 is not None:
            self.addNode(t1,t2)
        return t1 if t1 is not None else t2            

    def addNode(self,t1,t2):

        t1.val = t1.val + t2.val
        if t1.left is None:
            if t2.left is not None:
                t1.left = t2.left
            

        
        elif t2.left is not None:
            self.addNode(t1.left,t2.left)
        
        if t1.right is None:
            if t2.right is not None:
                t1.right = t2.right
        
        elif t2.right is not None:
            self.addNode(t1.right,t2.right)
        

        

        


        
        
        
        


