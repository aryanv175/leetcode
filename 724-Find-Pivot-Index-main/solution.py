# 724-Find-Pivot-Index-main 
""" Logic: Have two sum values, left sum and 
           right sum, iterate throught the  
           entire array assuming that the current
           element is the pivot index until one
           value actually is found out to be the 
           pivot index. Once it is found, return
           the index value. """

def pivotIndex(self, nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    left, right = 0, 0
    for j in range(len(nums)):
        right =  total - nums[j] - left
        if left == right:
            return j
        left += nums[j]
    return - 1
