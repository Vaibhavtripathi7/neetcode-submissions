from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        row = len(grid)
        col = len(grid[0])
        INF = 2147483647
        queue = deque()

        for i in range(row):
            for k in range(col):
                if grid[i][k] == 0:
                    queue.append((i,k))
        
        directions = [[0,-1],[-1,0],[0,1],[1,0]]

        while queue:

            r, c = queue.popleft()
            for dr,dc in directions: 
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= row or nc < 0 or nc >= col or grid[nr][nc] != INF:
                    continue

                grid[nr][nc] = grid[r][c] + 1 
                queue.append((nr,nc))
