class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # find middle element first or index:
        left = 0 
        right = len(nums) - 1 
        def binarysearch(left, right):
            if left > right: 
                return -1 
            mid = left + (right - left) // 2

            if (nums[mid] == target):
                return mid
            if (target > nums[mid]):
                return binarysearch( mid + 1, right)
            else:
                return binarysearch( left, mid - 1 )

        return binarysearch( left, right)

