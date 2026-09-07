class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x

        i_x = 1 # << shift to left by 1 for each bit location in x
        i_n = 1 # << shift to left by 1 for each bit location in x

        while i_n <= n - 1:
            if i_x & x == 0:
                if i_n & (n - 1):
                    res = res | i_x
                i_n = i_n << 1
            
            i_x <<= 1
        
        return res
