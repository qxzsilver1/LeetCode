class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = []

        for l, r, h in buildings:
            edges.append([l, h])
            edges.append([r, -h])
        edges.sort()

        live, past = [], []

        res = []

        idx = 0

        while idx < len(edges):
            curr_x = edges[idx][0]

            while idx < len(edges) and edges[idx][0] == curr_x:
                height = edges[idx][1]

                if height > 0:
                    heapq.heappush(live, -height)
                else:
                    heapq.heappush(past, height)
                idx += 1
                
            while past and past[0] == live[0]:
                heapq.heappop(live)
                heapq.heappop(past)
                
            max_height = - live[0] if live else 0

            if not res or max_height != res[-1][1]:
                res.append([curr_x, max_height])
        
        return res
