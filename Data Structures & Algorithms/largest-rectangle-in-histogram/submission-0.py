class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # holds indices, heights increasing bottom to top
        max_area = 0
        
        for i, h in enumerate(heights):
            # current bar is smaller than stack top -> resolve the top bar's rectangle
            while stack and heights[stack[-1]] > h:
                top_idx = stack.pop()
                height = heights[top_idx]
                # right boundary = current index i
                # left boundary = new stack top, or -1 if empty
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, height * width)
            stack.append(i)
        
        # anything left in stack has no smaller bar to the right -> right boundary = n
        while stack:
            top_idx = stack.pop()
            height = heights[top_idx]
            width = len(heights) - stack[-1] - 1 if stack else len(heights)
            max_area = max(max_area, height * width)
        
        return max_area