class Solution:
    def __init__(self):
        self.cache = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # let's just add an element in the cost:
        # cost.insert(0,0)
        def mincost(i, cost):
            # now adding caching layer : for proper DP solution to get linear time complexity
            if i >= len(cost): return 0
            if i in self.cache: return self.cache[i]
            result = cost[i] + min(mincost(i+1, cost),mincost(i+2, cost)) 
            self.cache[i] = result
            return result

        return min(mincost(0,cost), mincost(1,cost))