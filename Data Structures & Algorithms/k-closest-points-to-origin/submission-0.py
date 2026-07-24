import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(a, b):
            return (a**2 + b**2)
        heap = []
        heapq.heapify(heap)
        
        for a, b in points:
            dist = distance(a, b)
            heapq.heappush(heap, (-dist, [a, b]))
            if (len(heap) > k):
                heapq.heappop(heap) 
        return [points for dist, points in heap]