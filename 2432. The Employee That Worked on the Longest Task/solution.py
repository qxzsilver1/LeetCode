class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev_time = 0

        max_hours = 0
        max_emp = 0
        
        for e in logs:
            if e[1] - prev_time > max_hours:
                max_emp = e[0]
                max_hours = e[1] - prev_time
            elif e[1] - prev_time == max_hours and e[0] < max_emp:
                max_emp = e[0]
            
            prev_time = e[1]
        
        return max_emp
