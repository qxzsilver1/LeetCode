class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        output = 0

        while l <= r:
            m = l + (r - l) // 2

            if m ** 2 > x:
                r = m - 1
            elif m ** 2 < x:
                l = m + 1
                output = m
            else:
                return m
        
        return output
