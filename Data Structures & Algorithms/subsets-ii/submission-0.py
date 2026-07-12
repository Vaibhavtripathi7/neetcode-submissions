class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrack(path, start_index):

            result.append(path[:])

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([],0)
        return result 