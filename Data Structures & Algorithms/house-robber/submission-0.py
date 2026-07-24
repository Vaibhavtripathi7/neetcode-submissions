class Solution:
    def rob(self, nums: List[int]) -> int:

        max_profit2 = nums[0]
        max_profit1 = max(nums[1], nums[0]) 

        if len(nums) == 1:
            return nums[0]

        for i in range(2, len(nums)):
            max_profit_c = max( nums[i]+max_profit2, max_profit1)
            max_profit2 = max_profit1
            max_profit1 = max_profit_c

        return max_profit1
