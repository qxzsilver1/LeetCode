class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        n = len(routes)
        adjList = [[] for _ in range(n)]
        stopToRoutes = defaultdict(list)
        
        for bus, route in enumerate(routes):
            for stop in route:
                stopToRoutes[stop].append(bus)

        if target not in stopToRoutes or source not in stopToRoutes:
            return -1

        hasEdge = [[False] * n for _ in range(n)]
        
        for buses in stopToRoutes.values():
            for i in range(len(buses)):
                for j in range(i + 1, len(buses)):
                    if hasEdge[buses[i]][buses[j]]:
                        continue
                    hasEdge[buses[i]][buses[j]] = True
                    hasEdge[buses[j]][buses[i]] = True
                    adjList[buses[i]].append(buses[j])
                    adjList[buses[j]].append(buses[i])

        q = deque([node for node in stopToRoutes[source]])
        res = 1
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in stopToRoutes[target]:
                    return res
                
                while adjList[node]:
                    nxtBus = adjList[node].pop()
                    if adjList[nxtBus]:
                        q.append(nxtBus)
            res += 1

        return -1
