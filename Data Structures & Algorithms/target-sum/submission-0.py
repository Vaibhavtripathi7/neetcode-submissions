class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}

        def ways(index, target): # it's 2-D dp problem : mind that so here are more than two states: 

            # base: return what ?
            if index == len(nums):
                if target == 0: return 1 
                else: return 0
            if (index,target) in cache: return cache[(index,target)] 
            result = ways(index + 1, target + nums[index]) + ways(index + 1, target - nums[index]) # how i track the index and sign
            cache[(index,target)] = result
            return result

        return ways(0,target)