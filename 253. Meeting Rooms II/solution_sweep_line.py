class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time_map = defaultdict(int)

        for interval in intervals:
            time_map[interval[0]] += 1
            time_map[interval[1]] -= 1
        
        curr_num_meetings, res = 0, 0

        for i in sorted(time_map.keys()):
            curr_num_meetings += time_map[i]
            res = max(res, curr_num_meetings)
        
        return res
