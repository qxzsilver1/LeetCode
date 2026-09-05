class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dist = 0

        while xor:
            dist += 1

            xor = xor & (xor - 1)
        
        return dist
