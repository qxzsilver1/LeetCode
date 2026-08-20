class DisjointSetUnion:
    def __init__(self, n):
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
        
        if self.size[parent_u] < self.size[parent_v]:
            parent_u, parent_v = parent_v, parent_u
        
        self.size[parent_u] += self.size[parent_v]
        self.parent[parent_v] = parent_u

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        dsu = DisjointSetUnion(n)

        edges = []

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i+1, n):
                x2, y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist, i, j))
        
        edges.sort()

        total_cost = 0

        for dist, u, v in edges:
            if dsu.union(u, v):
                total_cost += dist
        
        return total_cost
