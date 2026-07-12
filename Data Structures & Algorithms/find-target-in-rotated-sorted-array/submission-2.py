class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 
        nums = nums 
        target = target 
        while left <= right: 
            mid = left + (right-left)//2
            if nums[mid] == target: 
                return mid

            elif nums[left] <= nums[mid]: # means left half sorted
                #now check for target in left half or not 
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 
                else: 
                    left = mid + 1 
            else: # here means right half sorted 
                if nums[mid] < target  <= nums[right]:
                    left = mid + 1 
                else: 
                    right = mid - 1
        
        return -1 
            