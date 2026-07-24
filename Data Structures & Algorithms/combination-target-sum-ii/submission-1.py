class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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

            for i in range(start_index, len(candidates) ):

                path.append(candidates[i])
                backtrack(path, target, i+1)
                path.pop()

        backtrack([], target, 0)

        return result