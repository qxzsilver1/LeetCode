class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        return n - 1 - abs(n - 1 - k % (2*n - 2))
