class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        graph = defaultdict(set)
        q = deque([(source, 0)])

        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)
        
        stop_visited, bus_visited = set(), set()

        while q:
            stop, route_length = q.popleft()

            if stop == target:
                return route_length
            
            for bus in graph[stop]:
                if bus not in bus_visited:
                    bus_visited.add(bus)

                    for stop in routes[bus]:
                        if stop not in stop_visited:
                            stop_visited.add(stop)
                            q.append((stop, route_length + 1))
        
        return -1
