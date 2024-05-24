class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        i = 0

        while num:
            if not (num & 1):
                res += 1 << i
            
            i += 1
            num >>= 1
        
        return res
