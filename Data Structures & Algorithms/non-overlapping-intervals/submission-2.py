class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[1])
        prevEnd = intervals[0][1]
        cnt = 0
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                cnt+=1
                prevEnd = min(intervals[i][1], prevEnd)
            else:
                prevEnd = intervals[i][1]
        return cnt
            
                