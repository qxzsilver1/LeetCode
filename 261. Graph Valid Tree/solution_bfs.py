class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj_list = [[] for _ in range(n)]

        for s, t in edges:
            adj_list[s].append(t)
            adj_list[t].append(s)
        
        visited = set()

        q = deque([(0, -1)])
        visited.add(0)

        while q:
            node, prev = q.popleft()

            for nei in adj_list[node]:
                if nei == prev:
                    continue
                
                if nei in visited:
                    return False
                
                visited.add(nei)
                q.append((nei, node))
        
        return len(visited) == n
