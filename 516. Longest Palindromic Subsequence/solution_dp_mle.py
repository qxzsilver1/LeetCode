class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def dfs(l, r):
            if l < 0 or r == len(s):
                return 0
            
            if (l, r) in cache:
                return cache[(l, r)]
            
            if s[l] == s[r]:
                lps_length = 1 if l == r else 2
                cache[(l, r)] = lps_length + dfs(l - 1, r + 1)
            else:
                cache[(l, r)] = max(dfs(l - 1, r), dfs(l, r + 1))
            
            return cache[(l, r)]
        
        for i in range(len(s)):
            dfs(i, i) # odd length
            dfs(i, i+1) # even length
        
        return max(cache.values())
