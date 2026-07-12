class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = []
        for i in range(0, len(nums)):
            if nums[i] == val:
                size.append(nums[i])
        for j in range(0, len(size)):
            nums.remove(size[j])
        
        return len(nums)