class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        def backtrack(path, target, start_index):
            sum = 0
            for j in path: 
                sum = sum + j
            if sum == target: 
                result.append(path[:])
                return

            if sum > target:
                return

            for i in range(start_index, len(nums) ):

                path.append(nums[i])
                backtrack(path, target, i)
                path.pop()

        backtrack([], target, 0)

        return result