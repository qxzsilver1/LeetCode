class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dvd = abs(dividend)
        dvsr = abs(divisor)

        res = 0

        while dvd >= dvsr:
            tmp = dvsr
            mult = 1

            while dvd >= tmp:
                dvd -= tmp
                res += mult

                mult += mult
                tmp += tmp
        
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res *= -1
        
        return min(2147483647, max(-2147483648, res))
