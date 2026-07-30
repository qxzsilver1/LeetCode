class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * (n + 1)

        cycle = set()
        cycleStart = -1

        def dfs(node, par):
            nonlocal cycleStart
            
            if visited[node]:
                cycleStart = node
                return True

            visited[node] = True
            
            for nei in adj_list[node]:
                if nei == par:
                    continue
                
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    
                    if node == cycleStart:
                        cycleStart = -1
                    
                    return True
            
            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []
