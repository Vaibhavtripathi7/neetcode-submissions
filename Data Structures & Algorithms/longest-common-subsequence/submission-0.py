class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = {}
        def lcs( i , j): 

            # first write base case : mind that we return length of the LCS: not LCS itself

            if i == len(text1) or j == len(text2): return 0 
            if (i,j) in cache: return cache[(i,j)]

            if text1[i] == text2[j]: 
                result = 1 + lcs(i+1, j+1)
            else: 
                result = max(lcs(i+1, j), lcs(i, j+1))
            
            cache[(i,j)] = result
            return result
        return lcs(0,0)