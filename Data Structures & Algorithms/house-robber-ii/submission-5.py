class Solution:

    def rob(self, nums: List[int]) -> int:
        cache = {}
        if len(nums) == 1: return nums[0]
        def maxrob(i,nums,cache):
            if i >= len(nums): return 0 #d base case
            if i in cache: return cache[i]
            result = max(nums[i] + (maxrob(i+2, nums, cache)), maxrob(i+1, nums,cache))
            cache[i] = result
            return result
        # i am overcomplicating the problem : maybe 
        cache1 = {}
        result1 = maxrob(0, nums[1:], cache1)
        cache2 = {}
        result2 = maxrob(0, nums[:-1], cache2)
        return max(result1, result2)
        # return max(maxrob)
        # return maxrob