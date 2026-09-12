class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 2:
            return num
        
        res = 0
        mul = 1

        for i in range(9, 1, -1):
            while num % i == 0:
                num //= i
                res = mul * i + res
                mul *= 10
        
        return res if num < 2 and res <= 2 ** 31 - 1 else 0
