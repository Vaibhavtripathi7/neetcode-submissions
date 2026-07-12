class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = 0

        for i in nums:
            if i == 0:
                a += 1
            elif i == 1:
                b += 1
            elif i == 2:
                c += 1  
        
        nums.clear()
        nums.extend([0 for i in range(a)])
        nums.extend([1 for i in range(b)])
        nums.extend([2 for i in range(c)])


        