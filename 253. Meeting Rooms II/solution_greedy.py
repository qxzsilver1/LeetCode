class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []

        for interval in intervals:
            times.append((interval[0], 1))
            times.append((interval[1], -1))
        
        times.sort(key= lambda x: (x[0], x[1]))

        curr_count, res = 0, 0

        for time in times:
            curr_count += time[1]
            res = max(res, curr_count)
        
        return res
