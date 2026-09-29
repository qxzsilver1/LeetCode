class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        def timeToMin(t):
            h, m = map(int, t.split(':'))
            return 60 * h + m
        
        res = 24 * 60 - timeToMin(timePoints[-1]) + timeToMin(timePoints[0])

        exists = [False] * (60 * 24)
        first_minute, last_minute = 60 * 24, 0

        for t in timePoints:
            m = timeToMin(t)
            
            if exists[m]:
                return 0
            
            exists[m] = True

            first_minute = min(first_minute, m)
            last_minute = max(last_minute, m)
        
        res = 60 * 24 - last_minute + first_minute
        
        prev_m = first_minute

        for m in range(first_minute + 1, len(exists)):
            if exists[m]:
                diff = m - prev_m
                res = min(res, diff)
                prev_m = m
        
        return res
