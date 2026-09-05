class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        res = []
        inserted = False

        for interval in intervals:

            # Current interval is completely before newInterval
            if interval[1] < newInterval[0]:
                res.append(interval)

            # Current interval is completely after newInterval
            elif interval[0] > newInterval[1]:
                
                if not inserted:
                    res.append(newInterval)
                    inserted = True

                res.append(interval)

            # They overlap
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        if not inserted:
            res.append(newInterval)

        return res