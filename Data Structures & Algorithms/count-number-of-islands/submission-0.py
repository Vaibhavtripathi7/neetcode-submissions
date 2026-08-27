class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        col = len(grid[0])
        count = 0
        visited = set()

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= col or grid[r][c] == "0" or (r,c) in visited: 
                return 

            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(rows): 
            for k in range(col):
                if grid[i][k] == "1" and (i,k) not in visited: 
                    dfs(i,k)
                    count +=1 

        return count