class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sweep_map = defaultdict(int)

        for start, end in intervals:
            sweep_map[start] += 1
            sweep_map[end] -= 1
        
        res = []

        interval = []

        num_active = 0

        for i in sorted(sweep_map):
            if not interval:
                interval.append(i)
            
            num_active += sweep_map[i]

            if num_active == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        
        return res
