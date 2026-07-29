class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        visited = [False] * n

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def bfs(node):
            q = deque([node])
            visited[node] = True

            while q:
                curr = q.popleft()

                for nei in adj_list[curr]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
        
        res = 0

        for i in range(n):
            if not visited[i]:
                bfs(i)
                res += 1
        
        return res
