class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float(inf)] * (n+1)
        dp[0] = 0

        for i, interval in enumerate(ranges):
            left, right = max(0, i - interval), min(n, i + interval)
        
            for j in range(left, right+1):
                dp[j] = min(dp[j], dp[left] + 1)
        
        return dp[n] if dp[n] != float(inf) else -1
