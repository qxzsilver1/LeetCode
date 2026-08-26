class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        line_sweep_map = defaultdict(int)

        for start, end in firstList:
            line_sweep_map[start] += 1
            line_sweep_map[end + 1] -= 1
        
        for start, end in secondList:
            line_sweep_map[start] += 1
            line_sweep_map[end + 1] -= 1
        
        res = []

        active = 0

        prev = None

        for x in sorted(line_sweep_map):
            if active == 2:
                res.append([prev, x - 1])
            
            active += line_sweep_map[x]
            prev = x
        
        return res
