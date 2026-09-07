class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [1]
        MOD = 10 ** 9 + 7

        prev = {}

        for i, c in enumerate(s):
            dp.append(dp[-1] * 2)

            if c in prev:
                dp[-1] -= dp[prev[c]]
            
            prev[c] = i
        
        return (dp[-1] - 1) % MOD
