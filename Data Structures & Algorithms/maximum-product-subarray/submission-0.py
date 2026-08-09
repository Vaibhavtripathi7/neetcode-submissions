class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        maxend = nums[0]
        minend = nums[0]

        for i in range(1,len(nums)): 
            candidate1 = nums[i]
            candidate2 = maxend * nums[i]
            candidate3 = minend * nums[i]

            maxend = max(candidate1, candidate2, candidate3)
            minend = min(candidate1, candidate2, candidate3)

            result = max(maxend, result)
        return result