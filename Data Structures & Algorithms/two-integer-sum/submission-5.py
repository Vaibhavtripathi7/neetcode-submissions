class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0 
        j = len(nums) - 1 
        while i<=j: 
            current_sum = nums[i] + nums[j]
            if (current_sum > target ): 
                j = j - 1 
            elif (current_sum < target):
                i = i + 1 
            elif (current_sum == target):
                return [i, j]