class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1 = 0
        cache = {}
        for i in nums:
            sum1 = sum1 + i

        if sum1 % 2 != 0: return False
        else: target = sum1 / 2 
        def partition(index, target):

            # reoccurence reln : every num have two chocie to include or not 
            # but include only when it's lower than target:
            # base cases: 
            if target == 0 : return True 
            if target in cache: return cache[target]
            if index == len(nums): 
                if target != 0:
                    return False
            if nums[index] <= target: 
                result = partition(index + 1, target - nums[index]) or partition(index +1, target)
            else: 
                result = partition(index +1, target)
            cache[target] = result
            return result

        return partition(0, target)