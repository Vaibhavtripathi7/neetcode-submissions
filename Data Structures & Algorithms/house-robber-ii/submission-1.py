class Solution:
    def __init__(self):
        self.cache = {}


    def rob(self, nums: List[int]) -> int:
        def maxrob(i,nums):
            if i >= len(nums): return 0 # base case
            if i in self.cache: return self.cache[i]
            result = max(nums[i] + (maxrob(i+2, nums)), maxrob(i+1, nums))
            self.cache[i] = result
            return result

        return max(maxrob(0, nums) - nums[0], maxrob(1, nums))
        # return max(maxrob)
        # return maxrob