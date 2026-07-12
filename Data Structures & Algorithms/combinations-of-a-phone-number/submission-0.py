class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        def backtrack(path, start_index):

            if (len(path) == len(digits)): 
                result.append(path)
                return
            for c in mapping[digits[start_index]]:
                backtrack(path + c, start_index + 1)

        backtrack("", 0)

        return result