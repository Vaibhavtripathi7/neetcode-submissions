class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0
        j = len(heights) - 1 
        res = 0

        while i<j:
            # find the volume:
            if (heights[i] < heights[j]):
                vol = heights[i] * (j - i)
                if (vol > res): 
                    res = vol
                i += 1  
            else: 
                vol = heights[j] * (j - i)
                if (vol > res): 
                    res = vol
                j -= 1
        
        return res
             