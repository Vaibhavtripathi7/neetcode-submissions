class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # How to sort the array: binary sort : quick sort: heap sort 
        list_ = []
        nums = sorted(nums)

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            
            if i > 0 and nums[i] == nums[i-1]:
                continue
    
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    list_.append([nums[i], nums[j], nums[k]])
                    # skip duplicates for j and k here
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return list_