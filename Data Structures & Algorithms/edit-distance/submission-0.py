class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # the issue is : i am taking the string with me -- using 1-D DP 
        # but i need to go with 2-D DP -- that's also the pattern -- 
        # using both indexes: let's write an reoccurence relation first: 
        cache = {}
        def same(index1, index2, word1, word2, cache): 
            # here we should also do the changes: 
            # to word1 and word2 -- acording to the operations choosen:
            # base case: 
            if  index2 == len(word2) : return len(word1) - index1 
            if index1 == len(word1): return len(word2) - index2

            if (index1, index2) in cache: return cache[(index1, index2)]

                # we have three operations
            if word1[index1] == word2[index2]:
                result = same(index1 + 1, index2+1, word1, word2, cache)
            else: 
                    # we have three options that store result 
                result = 1 + min(same(index1 +1, index2, word1, word2, cache), same(index1, index2 + 1, word1, word2, cache), same(index1+1 , index2 + 1, word1, word2, cache))
            cache[(index1, index2)] = result         
            return result
        return same(0,0, word1, word2, cache)