class Solution:
    def treeDiameter(self, edges: list[list[int]]) -> int:
        graph = [set() for i in range(len(edges)+1)]
        
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        def bfs(start):
            visited = [False] * len(graph)

            visited[start] = True
            q = deque([start])

            dist = -1
            last_node = start

            while q:
                next_q = deque()

                while q:
                    next_node = q.popleft()

                    for nei in graph[next_node]:
                        if not visited[nei]:
                            visited[nei] = True
                            next_q.append(nei)
                            last_node = nei
                dist += 1
                q = next_q
            
            return last_node, dist
        
        farthest_node, distance1 = bfs(0)
        other_farthest_node, distance2 = bfs(farthest_node)

        return distance2

        return diameter
                
