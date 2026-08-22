class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 *stone)
        while len(heap) > 1:
            st1 = heapq.heappop(heap)
            st2 = heapq.heappop(heap)
            if st1 < st2:
                heapq.heappush(heap, -1*(st2-st1))
        return (-1*heap[0]) if len(heap) > 0 else 0