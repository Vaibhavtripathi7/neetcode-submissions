class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        num = nums
        tar = target 
        # find middle element first or index:
        left = 0 
        right = len(nums) - 1 

        while True: 
            if left > right: 
                return -1
            mid = left + (right - left)//2 

            if num[mid] == tar:
                return mid
            elif num[mid] > tar: 
                right = mid - 1 
            else: 
                left = mid + 1  