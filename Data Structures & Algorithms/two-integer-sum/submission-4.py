class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0 
        j = len(nums) - 1 
        while i<=j: 
            
            remaining = target - nums[i]
            if (nums[j] > remaining ): 
                j = j - 1 
            elif (nums[j] < remaining):
                i = i + 1 
            elif (nums[j] == remaining):
                return [i, j]