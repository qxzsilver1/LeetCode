class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [float('inf')] * (4 * n)
        self.lazy = [float('inf')] * (4 * n)
    
    def propagate(self, tree_idx, lo, hi):
        if self.lazy[tree_idx] != float('inf'):
            self.tree[tree_idx] = min(self.tree[tree_idx], self.lazy[tree_idx])
            
            if lo != hi:
                self.lazy[2 * tree_idx + 1] = min(self.lazy[2 * tree_idx + 1], self.lazy[tree_idx])
                self.lazy[2 * tree_idx + 2] = min(self.lazy[2 * tree_idx + 2], self.lazy[tree_idx])
            self.lazy[tree_idx] = float('inf')
    
    def update(self, tree_idx, lo, hi, left, right, val):
        self.propagate(tree_idx, lo, hi)

        if lo > right or hi < left:
            return
        
        if lo >= left and hi <= right:
            self.lazy[tree_idx] = min(self.lazy[tree_idx], val)
            self.propagate(tree_idx, lo, hi)
            return
        
        mid = (lo + hi) // 2
        self.update(2 * tree_idx + 1, lo, mid, left, right, val)
        self.update(2 * tree_idx + 2, mid + 1, hi, left, right, val)
        self.tree[tree_idx] = min(self.tree[2 * tree_idx + 1], self.tree[2 * tree_idx + 2])
    
    def query(self, tree_idx, lo, hi, idx):
        self.propagate(tree_idx, lo, hi)
        
        if lo == hi:
            return self.tree[tree_idx]
        
        mid = (lo + hi) // 2
        
        if idx <= mid:
            return self.query(2 * tree_idx + 1, lo, mid, idx)
        else:
            return self.query(2 * tree_idx + 2, mid + 1, hi, idx)
    
    def update_range(self, left, right, val):
        self.update(0, 0, self.n - 1, left, right, val)

    def query_point(self, idx):
        return self.query(0, 0, self.n - 1, idx)

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        points = []
        
        for interval in intervals:
            points.append(interval[0])
            points.append(interval[1])
        
        for q in queries:
            points.append(q)
        
        points = sorted(set(points))
        compressed = {points[i]: i for i in range(len(points))}

        seg_tree = SegmentTree(len(points))

        for interval in intervals:
            start = compressed[interval[0]]
            end = compressed[interval[1]]
            length = interval[1] - interval[0] + 1
            seg_tree.update_range(start, end, length)
        
        ans = []
        
        for q in queries:
            idx = compressed[q]

            res = seg_tree.query_point(idx)
            ans.append(res if res != float('inf') else -1)
        
        return ans
