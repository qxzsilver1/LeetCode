class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()

        n = len(events)

        dp = [[-1] * n for _ in range(k + 1)]

        def dfs(i, cnt, prev_end_time):
            if i == n or cnt == k:
                return 0
            
            if events[i][0] <= prev_end_time:
                return dfs(i + 1, cnt, prev_end_time)
            
            if dp[cnt][i] != -1:
                return dp[cnt][i]
            
            dp[cnt][i] = max(dfs(i + 1, cnt, prev_end_time), dfs(i + 1, cnt + 1, events[i][1]) + events[i][2])

            return dp[cnt][i]
        
        return dfs(0, 0, -1)
