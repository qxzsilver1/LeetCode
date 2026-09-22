class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        times = []

        for e in events:
            times.append([e[0], 1, e[2]])
            times.append([e[1] + 1, 0, e[2]])
        
        res = 0
        max_val = 0
        times.sort()

        for t in times:
            if t[1]:
                res = max(res, t[2] + max_val)
            else:
                max_val = max(max_val, t[2])
        
        return res
