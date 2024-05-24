class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (1 << 30) % n
