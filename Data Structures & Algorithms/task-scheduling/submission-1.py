class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        A:3 
        B:1
        C:1
        Counter = {[3,A], [1,B], [1, C]}
        cooldown 
        we also need to keep track of cooldown time
        A
        '''
        cnt = Counter(tasks)
        heap = []
        for c in cnt.values():
            heapq.heappush(heap, -c)
        time = 0
        q = deque()

        while heap or q:
            time+=1
            if heap:
                c = 1 + heapq.heappop(heap)
                if c:
                    q.append([c, time+n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time




