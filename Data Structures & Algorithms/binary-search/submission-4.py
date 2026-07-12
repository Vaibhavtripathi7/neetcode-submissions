class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # num = nums
        # tar = target 
        # find middle element first or index:
        left = 0 
        right = len(nums) - 1 

        while True: 
            mid = left + (right - left)//2 
            if left > right: 
                return -1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: 
                right = mid - 1 
            else: 
                left = mid + 1  