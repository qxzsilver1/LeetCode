class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()

        n = len(events)

        start_times = [start for start, _, _ in events]

        dp = [[0] * (n + 1) for _ in range(k + 1)]

        for i in range(n - 1, -1, -1):
            for cnt in range(1, k + 1):
                next_idx = bisect_right(start_times, events[i][1])
                dp[cnt][i] = max(dp[cnt][i + 1], events[i][2] + dp[cnt - 1][next_idx])
        
        return dp[k][0]
