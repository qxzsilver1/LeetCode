class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        is_palindrome = [[False] * n for _ in range(n)]

        for pal_length in range(1, n + 1):
            for l in range(n - pal_length + 1):
                r = l + pal_length - 1

                is_palindrome[l][r] = s[l] == s[r] and (pal_length <= 2 or is_palindrome[l + 1][r - 1])
        
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            for j in range(i - k + 1):
                if is_palindrome[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return dp[n]
