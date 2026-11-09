class Solution:
    def findDerangement(self, n: int) -> int:
        mul, res = 1, 0
        MOD = 10 ** 9 + 7

        for i in range(n, -1, -1):
            val = 1 if i % 2 == 0 else -1
            res = (res + MOD + mul * val) % MOD
            mul = (mul * i) % MOD
        
        return res
