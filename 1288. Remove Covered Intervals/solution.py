class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: (x[0], - x[1]))

        res = [intervals[0]]

        for l, r in intervals[1:]:
            prev_l, prev_r = res[-1]

            if prev_l <= l and prev_r >= r:
                continue
            
            res.append([l, r])
        
        return len(res)
