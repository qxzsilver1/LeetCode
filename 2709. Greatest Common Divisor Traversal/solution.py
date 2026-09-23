class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        
        return self.par[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return
        
        if self.size[px] < self.size[py]:
            self.par[px] = py
            self.size[py] += self.size[px]
        else:
            self.par[py] = px
            self.size[px] += self.size[py]

        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        
        factor_to_idx = {}

        for i, num in enumerate(nums):
            f = 2

            while f * f <= num:
                if num % f == 0:
                    if f in factor_to_idx:
                        uf.union(i, factor_to_idx[f])
                    else:
                        factor_to_idx[f] = i
                    
                    while num % f == 0:
                        num //= f

                f += 1
            
            if num > 1:
                if num in factor_to_idx:
                    uf.union(i, factor_to_idx[num])
                else:
                    factor_to_idx[num] = i
        
        return uf.count == 1
