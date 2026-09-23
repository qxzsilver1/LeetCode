class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.size[px] += self.size[py]
        self.parent[py] = px

        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        N = len(nums)

        if N == 1:
            return True
        
        if any(num == 1 for num in nums):
            return False
        
        MAX = max(nums)
        sieve = [0] * (MAX + 1)
        p = 2
        while p * p <= MAX:
            if sieve[p] == 0:
                for composite in range(p * p, MAX + 1, p):
                    sieve[composite] = p
            p += 1

        uf = UnionFind(N + MAX + 1)
        
        for i in range(N):
            num = nums[i]
            if sieve[num] == 0:  # num is prime
                uf.union(i, N + num)
                continue

            while num > 1:
                prime = sieve[num] if sieve[num] != 0 else num
                uf.union(i, N + prime)
                while num % prime == 0:
                    num //= prime

        root = uf.find(0)
        for i in range(1, N):
            if uf.find(i) != root:
                return False
        return True
