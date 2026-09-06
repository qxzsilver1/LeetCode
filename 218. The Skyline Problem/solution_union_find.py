class DisjointSetUnion():
    def __init__(self, N):
        self.parent = list(range(N))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[x] = self.parent[y]

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = sorted(list(set([x for building in buildings for x in building[:2]])))

        edge_idx_map = { x: idx for idx, x in enumerate(edges)}
        
        buildings.sort(key = lambda x: -x[2])

        n = len(edges)
        dsu = DisjointSetUnion(n)

        heights = [0] * n

        for left_edge, right_edge, height in buildings:
            left_idx, right_idx = edge_idx_map[left_edge], edge_idx_map[right_edge]

            while left_idx < right_idx:
                left_idx = dsu.find(left_idx)

                if left_idx < right_idx:
                    dsu.union(left_idx, right_idx)
                    heights[left_idx] = height
                    left_idx += 1
        
        res = []

        for i in range(n):
            if i == 0 or heights[i] != heights[i - 1]:
                res.append([edges[i], heights[i]])
        
        return res
