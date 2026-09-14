class Solution:
    def maximumTeamSize(self, startTime: list[int], endTime: list[int]) -> int:
        intervals = list(zip(startTime, endTime))
        intervals.sort()

        n = len(intervals)

        mp = defaultdict(int)

        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]

            l = i + 1
            r = n - 1
            res = -1

            while l <= r:
                m = l + (r - l) // 2
                if intervals[m][0] > end:
                    res = m
                    r = m - 1
                else:
                    l = m + 1
            
            if res != -1:
                mp[intervals[i]] = n - res
        
        intervals.sort(key=lambda x: (x[1], x[0]))

        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]

            l = 0
            r = i - 1
            res = -1

            while l <= r:
                m = l + (r - l) // 2
                if intervals[m][1] < start:
                    res = m
                    l = m + 1
                else:
                    r = m - 1

            if res != -1:
                mp[intervals[i]] += (res + 1)
        
        res = 0
        
        for k, v in sorted(mp.items()):
            res = max(res, n - v + 1)
        
        return res
