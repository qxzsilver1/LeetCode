class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for parity in range(2):
                new_parity = (parity + arr[i]) % 2
                dp[i][parity] = (new_parity + dp[i + 1][new_parity]) % MOD

        res = 0
        
        for i in range(n):
            res = (res + dp[i][0]) % MOD
        
        return res
