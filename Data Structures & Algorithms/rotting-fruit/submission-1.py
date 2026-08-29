class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        visited = set()
        fresh_count = 0
        minutes = 0  

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2: 
                    queue.append((i,j)) # that's the start point: for multi source BFS
                elif grid[i][j] == 1: 
                    fresh_count += 1 

        directions = [[0,1],[0,-1],[-1,0],[1,0]] # all directions: 

        # now the count: var --we increment it when -- we pass one level 
        while queue and fresh_count > 0:
            level_nodes = len(queue) 
            for _ in range(level_nodes):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc # all four directions 
                    # one by one append in queue too : 
                    # now we check the cell : 
                    if nr < 0 or nc < 0 or nr >= row or nc >= col or (nr,nc) in visited or grid[nr][nc] != 1:
                        continue
                    visited.add((nr,nc))
                    fresh_count -= 1 
                    queue.append((nr,nc))
            minutes += 1
        return -1 if fresh_count > 0 else minutes 