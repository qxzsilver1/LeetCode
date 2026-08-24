class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        str_len, pattern_len = len(s), len(p)

        if p == s or set(p) == {'*'}:
            return True
        
        if p == '' or s == '':
            return False
        
        dp = [[False] * (str_len + 1) for _ in range(pattern_len + 1)]
        dp[0][0] = True

        for p_idx in range(1, pattern_len + 1):
            if p[p_idx - 1] == '*':
                s_idx = 1

                while not dp[p_idx - 1][s_idx - 1] and s_idx < str_len + 1:
                    s_idx += 1
                
                dp[p_idx][s_idx - 1] = dp[p_idx - 1][s_idx - 1]

                while s_idx < str_len + 1:
                    dp[p_idx][s_idx] = True
                    s_idx += 1
                
            elif p[p_idx - 1] == '?':
                for s_idx in range(1, str_len + 1):
                    dp[p_idx][s_idx] = dp[p_idx - 1][s_idx - 1]
            
            else:
                for s_idx in range(1, str_len + 1):
                    dp[p_idx][s_idx] = dp[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]
        
        return dp[pattern_len][str_len]
