class Solution:
    def minCut(self, s: str) -> int:
        cuts_dp = [0] * len(s)

        for i in range(1, len(s)):
            cuts_dp[i] = i
        
        def findMinimumCuts(start_idx, end_idx):
            while start_idx >= 0 and end_idx < len(s) and s[start_idx] == s[end_idx]:
                new_cut = 0 if start_idx == 0 else cuts_dp[start_idx - 1] + 1
                cuts_dp[end_idx] = min(cuts_dp[end_idx], new_cut)
                start_idx -= 1
                end_idx += 1
        
        for m in range(len(s)):
            findMinimumCuts(m, m)
            findMinimumCuts(m - 1, m)
        
        return cuts_dp[len(s) - 1]
