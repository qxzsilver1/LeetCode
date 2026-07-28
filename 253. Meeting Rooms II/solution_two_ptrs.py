class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        res = 0
        cnt = 0

        s, e = 0, 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                s += 1
                cnt += 1
            else:
                e += 1
                cnt -= 1
            
            res = max(res, cnt)
        
        return res
