class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def dfs(l, r):
            if l < 0 or r == n:
                return 0
            
            if dp[l][r] != -1:
                return dp[l][r]

            if s[l] == s[r]:
                lps_length = 1 if l == r else 2
                dp[l][r] = lps_length + dfs(l - 1, r + 1)
            else:
                dp[l][r] = max(dfs(l - 1, r), dfs(l, r + 1))

            return dp[l][r]

        for i in range(n):
            dfs(i, i)  # odd length
            dfs(i, i + 1)  # even length

        return max(max(row) for row in dp if row != -1)
