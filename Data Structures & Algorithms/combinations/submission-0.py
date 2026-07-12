class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(1, n+1 ):
            nums.append(i)

        result = []
        def backtrack(path, target, start_index):

            if len(path) == target: 
                result.append(path[:])
                return

            for i in range(start_index, n):
                path.append(nums[i])
                backtrack(path, target, i + 1)
                path.pop()

        backtrack([], k,0)
        return result