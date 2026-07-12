class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setoflist = set(nums)
        if (len(setoflist)< len(nums)):
            return True
        else:
            return False 