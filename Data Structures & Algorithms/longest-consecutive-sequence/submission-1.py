class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # I have to make a hash table:
        result = 0 
        if len(nums) == 0:
            return 0  
        dict_ = {}
        for i in range(len(nums)):
            dict_[nums[i]] = 0

        for i in nums:
            # i have to loop-up for the sequence check: 
            if (i-1) in dict_:
                continue
            else: 
                max_length = 0
                k = 1
                while (i + k) in dict_:
                    k += 1 
                    max_length += 1
                result = max(result, max_length)

        return result + 1 
