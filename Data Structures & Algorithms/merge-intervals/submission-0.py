class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        intervals.sort(key=lambda x: x[0])
        endTime = intervals[0][1]
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= endTime:
                res[len(res)-1][1] = max(res[len(res)-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
            endTime = max(intervals[i][1], res[len(res)-1][1])
        return res