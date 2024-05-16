class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins_a_day = 1440

        if len(timePoints) > mins_a_day:
            return 0
        
        def minutify(t):
            return 60 * int(t[:2]) + int(t[3:])
        
        time_buckets = [0] * mins_a_day

        for time in timePoints:
            mins = minutify(time)

            if time_buckets[mins]:
                return 0
            
            time_buckets[mins] = 1
        
        minutes = [i for i in range(mins_a_day) if time_buckets[i]]

        return min((minutes[i] - minutes[i-1]) % mins_a_day for i in range(len(minutes)))
        

        
