class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        for n1, n2 in edges:
            adj_list[n1 - 1].append(n2 - 1)
            adj_list[n2 - 1].append(n1 - 1)

        colors = [-1] * n

        visited = [False] * n

        def isBipartite(node):
            for nei in adj_list[node]:
                if colors[nei] == colors[node]:
                    return False
                
                if colors[nei] != -1:
                    continue
                
                colors[nei] = (colors[node] + 1) % 2

                if not isBipartite(nei):
                    return False
            
            return True
        
        def getLongestShortestPath(src):
            q = deque([src])

            visit = [False] * n
            visit[src] = True

            dist = 0

            while q:
                for _ in range(len(q)):
                    node = q.popleft()

                    for nei in adj_list[node]:
                        if visit[nei]:
                            continue
                        visit[nei] = True
                        q.append(nei)
                dist += 1
            
            return dist

        for node in range(n):
            if colors[node] != -1:
                continue
            
            colors[node] = 0

            if not isBipartite(node):
                return -1
        
        distances = [getLongestShortestPath(i) for i in range(n)]

        def getNumConnectedComponents(node):
            max_num_groups = distances[node]
            visited[node] = True

            for nei in adj_list[node]:
                if visited[nei]:
                    continue
                max_num_groups = max(max_num_groups, getNumConnectedComponents(nei))
            
            return max_num_groups

        max_groups = 0

        for node in range(n):
            if visited[node]:
                continue
            
            max_groups += getNumConnectedComponents(node)
        
        return max_groups
