class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1

        while x < n:
            if x == n:
                return True
            
            x *= 2
        
        return x == n
