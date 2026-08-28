INF = float('inf')

class SegmentTree:
    def __init__(self, A):
        self.A = A[:]
        self.n = len(A)
        while (self.n & (self.n - 1)) != 0:
            self.A.append(INF)
            self.n += 1

        self.tree = [0] * (2 * self.n)
        self.build()

    def build(self):
        for i in range(self.n):
            self.tree[self.n + i] = i
        for j in range(self.n - 1, 0, -1):
            a = self.tree[j << 1]
            b = self.tree[(j << 1) | 1]
            self.tree[j] = a if self.A[a] <= self.A[b] else b

    def update(self, i, val):
        self.A[i] = val
        j = (self.n + i) >> 1
        while j >= 1:
            a = self.tree[j << 1]
            b = self.tree[(j << 1) | 1]
            self.tree[j] = a if self.A[a] <= self.A[b] else b
            j >>= 1

    def query(self, ql, qh):
        return self._query(1, 0, self.n - 1, ql, qh)

    def _query(self, node, l, h, ql, qh):
        if ql > h or qh < l:
            return -1
        if l >= ql and h <= qh:
            return self.tree[node]
        mid = (l + h) >> 1
        a = self._query(node << 1, l, mid, ql, qh)
        b = self._query((node << 1) | 1, mid + 1, h, ql, qh)

        if a == -1: return b
        if b == -1: return a
        return a if self.A[a] <= self.A[b] else b

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        seg = SegmentTree(target)
        stack = [(0, len(target) - 1, 0)]
        res = 0

        while stack:
            l, r, h = stack.pop()
            if l > r:
                continue
            minIdx = seg.query(l, r)
            res += target[minIdx] - h
            stack.append((l, minIdx - 1, target[minIdx]))
            stack.append((minIdx + 1, r, target[minIdx]))

        return res
