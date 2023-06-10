# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def solve (root, level):
            if root:
                if len(res) == level:
                    res.append(root.val)
                solve(root.right, level+1)
                solve(root.left, level+1)
        
        res = []
        solve(root, 0)
        return res
