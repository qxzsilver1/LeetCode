class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        timePoints.sort()

        def timeToMin(t):
            h, m = map(int, t.split(':'))
            return 60 * h + m
        
        res = 24 * 60 - timeToMin(timePoints[-1]) + timeToMin(timePoints[0])

        for i in range(len(timePoints) - 1):
            curr = timeToMin(timePoints[i + 1])
            prev = timeToMin(timePoints[i])
            diff = curr - prev
            res = min(res, diff)
        
        return res
