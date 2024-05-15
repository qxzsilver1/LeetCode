class Solution:
    def mySqrt(self, x: int) -> int:
        n = 2

        while True:
            if n * n <= x < (n + 1) * (n + 1):
                return n
            
            z = (x - n ** 2) / (2 * n) + n

            n = int(z)
