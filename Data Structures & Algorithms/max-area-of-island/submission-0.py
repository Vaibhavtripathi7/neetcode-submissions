class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])
        max_area, count = 0, 0
        visited = set() 

        def dfs(r,c):
            nonlocal max_area, count
            if r <0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r,c) in visited: return 

            visited.add((r,c))
            count += 1

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c - 1)
            
            # if count > max_area: max_area = count
        
        for i in range(rows):
            for k in range(cols):

                if grid[i][k] == 1 and (i,k) not in visited:
                    count = 0 
                    dfs(i,k)
                    if count > max_area: max_area = count
        
        return max_area