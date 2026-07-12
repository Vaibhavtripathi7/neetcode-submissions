from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()
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
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(path, target, i+1)
                path.pop()

        backtrack([], target, 0)

        return result