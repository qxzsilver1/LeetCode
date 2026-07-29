class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(node):
            if node == parent[node]:
                return parent[node]
            
            parent[node] = find(parent[node])

            return parent[node]
        
        def union(u, v):
            p_u, p_v = find(u), find(v)

            if p_u == p_v:
                return False
            
            if rank[p_u] > rank[p_v]:
                parent[p_v] = p_u
                rank[p_u] += rank[p_v]
            else:
                parent[p_u] = p_v
                rank[p_v] += rank[p_u]
            
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
