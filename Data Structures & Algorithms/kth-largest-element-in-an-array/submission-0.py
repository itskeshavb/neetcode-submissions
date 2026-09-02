class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        rem = len(nums)-k
        while heap and rem > 0:
            heapq.heappop(heap)
            rem-=1
        return heap[0]