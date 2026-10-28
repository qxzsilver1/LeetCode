# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        hi = 1

        while reader.get(hi) < target:
            hi *= 2
        
        lo = 0

        while lo <= hi:
            m = (lo + hi) // 2

            val = reader.get(m)

            if val == target:
                return m
            
            if val < target:
                lo = m + 1
            else:
                hi = m - 1
        
        return -1
