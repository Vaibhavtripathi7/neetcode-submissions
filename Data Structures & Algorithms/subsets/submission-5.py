class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        total_result = []
        def backtrack(path ,start_index):
            
            total_result.append(path[:])

            for i in range(start_index, len(nums)):
                path.append(nums[i]) 
                backtrack(path, i + 1 )
                path.pop()

        backtrack([], 0)
        return total_result