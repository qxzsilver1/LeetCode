class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res, start, end = 1, intervals[0][0], intervals[0][1]

        for l, r in intervals:
            if start < l and end < r:
                start = l
                res += 1
            end = max(end, r)

        return res
