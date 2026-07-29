class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        visited = [False] * n

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(node):
            for nei in adj_list[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        res = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1
        
        return res
