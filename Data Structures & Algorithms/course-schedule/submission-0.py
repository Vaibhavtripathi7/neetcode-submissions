class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict_ = {i: [] for i in range(numCourses)}   # every node gets an empty list up front
        for a, b in prerequisites:
            dict_[b].append(a)      # b points to a
        # pattern is Grey, white, and black 
        white, black, grey = 0, 1, 2
        color = [white] * numCourses

        def dfs(node):
            color[node] = grey
            for i in dict_[node]:
                if color[i] == grey:
                    return True
                elif color[i] == white:
                    if dfs(i):
                        return True
            color[node] = black
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
            
        return True


