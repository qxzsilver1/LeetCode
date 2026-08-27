class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        
        if n < m:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False for _ in range(n + 1)]
        dp[n] = True

        for i in range(m, -1, -1):
            next_dp = [False for _ in range(n + 1)]
            
            if i == m:
                next_dp[n] = True
            
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i + j] and dp[j]:
                    next_dp[j] = True
                
                if j < n and s2[j] == s3[i + j] and next_dp[j + 1]:
                    next_dp[j] = True
                
            dp = next_dp
        
        return dp[0]
