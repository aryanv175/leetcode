# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # find the mid, if the lenght is 0 return None
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        # root is the middle one. 
        root = TreeNode(nums[mid])
        # all the elements to the left of mid should be root.left
        root.left = self.sortedArrayToBST(nums[:mid])
        # all the elements to the right of mid should be root.right
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root # return!

