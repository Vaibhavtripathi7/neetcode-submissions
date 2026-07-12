class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heights = heights
        left = 0
        right = len(heights) -1 
        res = 0

        while left<right: 

            if (heights[left] < heights[right]):
                vol = (heights[left]) * (right - left)
                if ( vol > res):
                    res = vol
                left += 1      

            else: 
                vol = (heights[right]) * (right - left)
                if (vol > res):
                    res = vol 
                right -= 1
        return res