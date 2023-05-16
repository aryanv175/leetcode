# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 98. Validate Binary Search Tree
""" Logic: Key Concept: Depth first search.
           We use a lower bound value and an upper bound value which are initialised
           as negative infinity and positive infinity respectively. These values
           change with every iteration. The lower bound takes the value of the root
           when we are implementing the function for the right child of the node and
           the upper bound takes the value of the root when we are implementing the
           function for the left child of the node."""

def isValidBST(root: Optional[TreeNode]) -> bool:

    def dfs(lower, upper, node):
        if not node:
            return True

        elif node.val <= lower or node.val>= upper:
            return False

        else:
            return dfs(lower, node.val, node.left) and dfs(node.val, upper, node.right)

    return dfs(float(-inf), float(inf), root)
