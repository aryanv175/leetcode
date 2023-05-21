# 1. Two Sum
"""Logic: using two pointers here. left and right. 
            we take the first pointer and check if the
            next pointer is at a number which is equal to
            the difference = target - nums[left]. If so, we 
            return the index."""
            

def twoSum(nums: List[int], target: int) -> List[int]:
    for left in range(len(nums)-1):
        for right in range(left+1, len(nums)):
            if target - nums[left] == nums[right]:
                return [left, right]
