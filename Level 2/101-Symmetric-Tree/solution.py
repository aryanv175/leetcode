# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if (root.left) and (not root.right) or (root.right) and (not root.left): 
            return False # if it does not have left node but has right node then you return False and vice versa.
        if (not root.left) and (not root.right):
            return True # if it only has one node, root. Return True
        
        lroot = root.left # we divide tree into two subtrees left and right
        rroot = root.right

        return self.checkEqual(lroot, rroot) # checkEqual function to check the trees
    
    def checkEqual(self, p, q):
        if p and q: # this function checks if p.left  === q.right
            return p.val == q.val and self.checkEqual(p.left, q.right) and self.checkEqual(p.right, q.left)
        return p is q # return!
