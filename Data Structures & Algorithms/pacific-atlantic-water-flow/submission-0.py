class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        bfs_queue = deque()
        pac_visited = set()
        atl_visited = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def bfs(queue, visited):
            # start : is a tuple i have to unpack it: 
            while queue: 
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # we have to check condition: 
                    if nr < 0 or nc < 0 or nr >= row or nc >= col or (nr,nc) in visited or heights[nr][nc] < heights[r][c]:
                        continue
                    visited.add((nr,nc))
                    queue.append((nr,nc))

        pac_queue = deque()
        atl_queue = deque()

        for r in range(row):
            pac_queue.append((r, 0))
            pac_visited.add((r,0))
            atl_queue.append((r, col-1))
            atl_visited.add((r, col-1))

        for c in range(col):
            pac_queue.append((0, c))
            pac_visited.add((0,c))
            atl_queue.append((row-1, c))
            atl_visited.add((row-1, c))

        bfs(pac_queue, pac_visited)
        bfs(atl_queue, atl_visited)

        return [[r,c] for r in range(row) for c in range(col) if (r,c) in pac_visited and (r,c) in atl_visited]


