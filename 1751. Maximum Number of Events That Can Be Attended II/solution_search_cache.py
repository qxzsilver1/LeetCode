class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()

        n = len(events)

        start_times = [start for start, _, _ in events]
        next_indices = [bisect_right(start_times, events[i][1]) for i in range(n)]

        dp = [[-1] * n for _ in range(k + 1)]

        def dfs(i, cnt):
            if cnt == k or i == n:
                return 0
            
            if dp[cnt][i] != -1:
                return dp[cnt][i]
            
            next_idx = next_indices[i]

            dp[cnt][i] = max(dfs(i + 1, cnt), events[i][2] + dfs(next_idx, cnt + 1))

            return dp[cnt][i]
        
        return dfs(0, 0)
