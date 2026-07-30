class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)

        start_max_end_map = [0] * (max_val + 1)

        for start, end in intervals:
            start_max_end_map[start] = max(end + 1, start_max_end_map[start])
        
        res = []

        curr_end = -1
        interval_start = -1

        for i in range(len(start_max_end_map)):
            if start_max_end_map[i] != 0:
                if interval_start == -1:
                    interval_start = i
                
                curr_end = max(start_max_end_map[i] - 1, curr_end)
            
            if curr_end == i:
                res.append([interval_start, curr_end])
                curr_end = -1
                interval_start = -1
        
        if interval_start != -1:
            res.append([interval_start, curr_end])
        
        return res
