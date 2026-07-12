class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dict_ = {i: [] for i in range(n) }
        for u, v in edges: 
            dict_[u].append(v)
            dict_[v].append(u)
        # so, adjency list ready here! 
        def dfs(node, graph):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i, graph)
        visited = set()
        count = 0 
        for i in dict_:
            if i not in visited:
                dfs(i, dict_)
                count += 1 

        return count 
