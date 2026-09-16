class Solution:
    def treeDiameter(self, edges: list[list[int]]) -> int:
        graph = [set() for i in range(len(edges)+1)]
        
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)
        
        diameter = 0

        visited = [False for i in range(len(graph))]

        def dfs(curr):
            nonlocal diameter

            top_distance1, top_distance2 = 0, 0

            dist = 0
            visited[curr] = True

            for nei in graph[curr]:
                if not visited[nei]:
                    dist = 1 + dfs(nei)
                
                if dist > top_distance1:
                    top_distance1, top_distance2 = dist, top_distance1
                elif dist > top_distance2:
                    top_distance2 = dist
            
            diameter = max(diameter, top_distance1 + top_distance2)

            return top_distance1
        
        dfs(0)

        return diameter
                
