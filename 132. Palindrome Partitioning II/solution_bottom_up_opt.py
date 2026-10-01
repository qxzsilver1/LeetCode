class Solution:
    def minCut(self, s: str) -> int:
        cuts_dp = [0] * len(s)
        palindrome_dp = [[0] * len(s) for _ in range(len(s))]

        for end in range(len(s)):
            min_cut = end
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or palindrome_dp[start + 1][end - 1]):
                    palindrome_dp[start][end] = 1
                    min_cut = 0 if start == 0 else min(min_cut, cuts_dp[start - 1] + 1)
            
            cuts_dp[end] = min_cut
        
        return cuts_dp[len(s) - 1]
