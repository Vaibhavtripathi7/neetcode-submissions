class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        total_result = [] 
        def backtrack(path ,length, start_index):

            if len(path) == length :
                total_result.append(path[:]) 
                return 

            
            for i in range(start_index, len(nums)): 
                path.append(nums[i])
                backtrack(path,length, i+1)
                path.pop()

        for length in range(len(nums) + 1 ):
            path= []
            val = 0
            backtrack(path, length, val)

        return total_result