"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        res = []

        min_heap = [(emp[0].start, emp_id, 0) for emp_id, emp in enumerate(schedule)]
        heapq.heapify(min_heap)
        prev_end = min(interval.start for emp in schedule for interval in emp)

        while min_heap:
            start, emp_id, job_idx = heapq.heappop(min_heap)

            if prev_end < start:
                res.append(Interval(prev_end, start))
            
            prev_end = max(prev_end, schedule[emp_id][job_idx].end)
            
            if job_idx + 1 < len(schedule[emp_id]):
                heapq.heappush(min_heap, (schedule[emp_id][job_idx+1].start, emp_id, job_idx+1))
        
        return res
