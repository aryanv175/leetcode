class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we will use binary search for optimal solution
        left, right = 0, len(nums) - 1 # assign the indexes. left at the start, right at th end
        while left <= right: # we continue the loop until left stays to the left of right
            mid = (left + right)//2 # mid the average of the two
            if nums[mid] == target: # if we find the target, we return it
                return mid
            
            if nums[mid] < nums[right]: 
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return - 1
