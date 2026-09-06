class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))

        res = []

        for pos in positions:
            max_height = 0

            for l, r, h in buildings:
                if l <= pos < r:
                    max_height = max(max_height, h)
            
            if not res or max_height != res[-1][1]:
                res.append([pos, max_height])
        
        return res
