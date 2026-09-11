class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0 

  
        while j < len(nums):
            if nums[j] != 0:
            # swap
                a = nums[j]
                nums[j] = nums[i]
                nums[i] = a
                i += 1 

            j += 1 