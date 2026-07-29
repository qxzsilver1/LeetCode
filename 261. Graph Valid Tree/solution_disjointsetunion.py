class DisjointSetUnion:
    def __init__(self, n):
        self.components = n
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u == parent_v:
            return False
        
        self.components -= 1

        if self.size[parent_u] < self.size[parent_v]:
            parent_u, parent_v = parent_v, parent_u
        
        self.size[parent_u] += self.size[parent_v]
        self.parent[parent_v] = parent_u

        return True
    
    def getComponents(self):
        return self.components

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        
        if not n:
            return True
        
        disjoint_set_union = DisjointSetUnion(n)

        for s, t in edges:
            if not disjoint_set_union.union(s, t):
                return False
        
        return disjoint_set_union.getComponents() == 1
