import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x,y = point
            dist = math.sqrt(math.pow(x,2) + math.pow(y,2))
            heapq.heappush(heap,(dist, point))
        res = []
        while heap and k > 0:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res