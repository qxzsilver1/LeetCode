class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        to_flip, bit = n, 1

        while to_flip:
            n ^= bit
            bit <<= 1
            to_flip >>= 1
        
        return n
