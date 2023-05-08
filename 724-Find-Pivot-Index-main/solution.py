class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
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
