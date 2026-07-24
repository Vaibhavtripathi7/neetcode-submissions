class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        stack = [] # this will store temperatures
        results = [0] *len(temp)
        for i in range(len(temp)):
            
            while stack and (temp[i] > temp[stack[-1]]):
                j = stack.pop()
                results[j] = i - j
            
            stack.append(i)

        return results
            