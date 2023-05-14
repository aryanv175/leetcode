
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
#589. N-ary Tree Preorder Traversal
""" Logic: Key concept: Depth first search.
           This problem is quite simple to do with
           a recursive function. We first start with
           the root of the tree and then simply do a 
           depth first search and append the value of
           the nodes as we go through the tree. """
          

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        result = []
        def depth_first_search(node):
            if not node:
                return 
            result.append(node.val)

            for child in node.children:
                depth_first_search(child)
            
        depth_first_search(root)

        return result
