class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums) -1 
        res = []
        result = -1 
        while left <= right: 
            mid = left + (right-left)//2
            if nums[mid] == target: 
                result = mid 
                right = mid - 1 # for lower bound
            elif nums[mid] > target: 
                right = mid - 1
            else: 
                left = mid + 1
        
        res.append(result)
        result = -1
        left = 0 
        right = len(nums) - 1  
        while left <=right : 
            mid = left + (right-left)// 2 
            if nums[mid] == target: 
                result = mid 
                left = mid + 1
            elif nums[mid] > target: 
                right = mid -1 
            else: 
                left = mid + 1 
        res.append(result)
        return res 
