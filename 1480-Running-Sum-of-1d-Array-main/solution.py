# 1480-Running-Sum-of-1d-Array-main 
""" Logic: One loop that goes through the array
           adds the previous element to the 
           current one. """

def runningSum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums
