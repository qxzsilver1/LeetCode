class Solution:
    def maximumTeamSize(self, startTime: list[int], endTime: list[int]) -> int:
        intervals = list(zip(startTime, endTime))

        events = []

        for s, e in intervals:
            events.append((s, 1))
            events.append((e, -1))
        
        events.sort(key= lambda x: (x[0], -x[1]))
        
        active = 0
        max_size = 0

        for x in events:
            active += x[1]
            max_size = max(max_size, active)
        
        return max_size
