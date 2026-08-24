class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        x, y = 6, 6

        for _ in range(2, n + 1):
            n_x = (3 * x + 2 * y) % MOD
            n_y = (2 * x + 2 * y) % MOD
            x, y = n_x, n_y
        
        return (x + y) % MOD
