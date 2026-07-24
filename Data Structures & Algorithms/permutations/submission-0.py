class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(path, target, start_index):

            if len(path) == target:
                result.append(path[:])
                return

            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtrack(path, target, i +1 )
                path.pop()

        backtrack([], len(nums), 0)
        return result