class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
        self.components = n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        p_u = self.find(u)
        p_v = self.find(v)

        if p_u == p_v:
            return False
        
        self.components -= 1

        if self.size[p_u] > self.size[p_v]:
            self.size[p_u] += self.size[p_v]
            self.parent[p_v] = p_u
        else:
            self.size[p_v] += self.size[p_u]
            self.parent[p_u] = p_v
        
        return True
    
    def numComponents(self):
        return self.components

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DisjointSetUnion(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    dsu.union(i, j)
        
        return dsu.numComponents()
