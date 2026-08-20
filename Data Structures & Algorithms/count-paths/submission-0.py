class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def ways(i,j):
            # now : what do we memoize : we do for each position answers: 
            # have two choices on each grid: 
            # base-case: one if out of bound and another is last or target case
            # now check for result using pos: 
            if i == m - 1 and j == n -1: return 1
            if i > m - 1 or j > n - 1: return 0
            pos1 = i * n + j 
            if pos1 in cache: return cache[pos1] 

            # that's the base case : sorted 
            # now we recurse and find the solution and add the answers : for all no of ways 

            result = ways(i + 1, j) + ways(i, j+1) # and we return the result 
            pos = i * n + j 
            cache[pos] = result # cache the result 
            return result
        return ways(0, 0)