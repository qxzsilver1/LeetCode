class Solution:
    def findDerangement(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a, b = 1, 0

        for i in range(2, n + 1):
            # same as 
            # a, b = b, (i-1)*(a+b) % MOD
            tmp_a = b
            tmp_b = (i-1)*(a+b) % MOD
            a = tmp_a
            b = tmp_b
        
        return b
