class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = []

        for i, building in enumerate(buildings):
            edges.append([building[0], i])
            edges.append([building[1], i])
        edges.sort()

        live = []
        res = []

        idx = 0

        while idx < len(edges):
            curr_x = edges[idx][0]

            while idx < len(edges) and edges[idx][0] == curr_x:
                b = edges[idx][1]

                if buildings[b][0] == curr_x:
                    right = buildings[b][1]
                    height = buildings[b][2]
                    heapq.heappush(live, [-height, right])
                
                while live and live[0][1] <= curr_x:
                    heapq.heappop(live)
                
                idx += 1
            max_height = - live [0][0] if live else 0

            if not res or max_height != res[-1][1]:
                res.append([curr_x, max_height])
        
        return res
