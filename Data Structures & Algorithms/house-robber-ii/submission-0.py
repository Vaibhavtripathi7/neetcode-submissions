class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def maxrob(i,nums):
            if i >= len(nums): return 0 # base case

            result = max(nums[i] + (maxrob(i+2, nums)), maxrob(i+1, nums))

            return result

        return max(maxrob(0, nums) - nums[0], maxrob(1, nums) )
        # return maxrob