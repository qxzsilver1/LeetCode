class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0

        i = 0

        for i in range(32):
            bit = (n >> i) & 1
            output |= (bit << (31-i))
        
        return output
