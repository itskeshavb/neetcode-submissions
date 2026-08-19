class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            if num not in mp:
                mp[num] = 1
            else:
                mp[num]+=1
        heap = []
        for key in mp.keys():
            heapq.heappush(heap, (mp[key],key))
        while len(heap) > k:
            heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res