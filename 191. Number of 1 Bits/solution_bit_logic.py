class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0

        while n:
            n &= (n-1)
            bit_count += 1
        
        return bit_count
