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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        disjoint_set_union = DisjointSetUnion(n)
        num_connected_components = n

        for c in connections:
            if disjoint_set_union.find(c[0]) != disjoint_set_union.find(c[1]):
                num_connected_components -= 1
                disjoint_set_union.union(c[0], c[1])
        
        return num_connected_components - 1
        
