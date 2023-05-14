# 102. Binary Tree Level Order Traversal
""" Logic: Key concept: Depth first search/defaultdict.
           The reason why use defaultdict and not dict
           is because default dict lets you access and
           edit the values of a key tha this not present
           in the dictionary. Once you understand this, 
           we basically make a dict{<level>: <node.val>}
           using dfs."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        
        d = defaultdict(list)
        def depth_first_search(node, level):
            if not node:
                return
            d[level].append(node.val)
            depth_first_search(node.left, level+1)
            depth_first_search(node.right, level+1)
        
        depth_first_search(root, 0)
        return d.values()
