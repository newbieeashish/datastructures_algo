'''Given the root node of a binary search tree (BST) and a value.
 You need to find the node in the BST that the node's value equals
  the given value. Return the subtree rooted with that node. If 
such node doesn't exist, you should return NULL.'''



class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        
        while cur is not None:
            
            if cur.val == val:
                #  hit
                return cur
            
            elif cur.val > val:
				# val is smaller than current node value, serach left sub-tree
                cur = cur.left
                
            else:
				# val is larger than current node value, serach right sub-tree
                cur = cur.right
        
        # miss
        return None



####Solution 2::::


class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            # miss
            return None
			
        else:
            if root.val == val: 
                # hit
                return root
				
            elif root.val > val: 
				# val is smaller than current node value, serach left sub-tree
                return self.searchBST(root.left, val)
				
            else:
				# val is larger than current node value, serach right sub-tree
                return self.searchBST(root.right, val)