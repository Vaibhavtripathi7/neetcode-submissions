class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = numbers
        i = 0 
        j = len(numbers) - 1 
        while i<j: 
            current_sum = numbers[i] + numbers[j]
            if (current_sum > target ): 
                j = j - 1 
            elif (current_sum < target):
                i = i + 1 
            elif (current_sum == target):
                return [i+1, j+1 ]