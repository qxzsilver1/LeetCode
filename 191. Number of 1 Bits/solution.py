class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0

        while n:
            bit_count += n & 1
            n = n >> 1
        
        return bit_count
