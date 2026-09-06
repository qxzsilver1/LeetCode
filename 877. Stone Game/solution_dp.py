class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        
        dp = piles[:]

        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(piles[left] - dp[left + 1], piles[right] - dp[left])
        
        return dp[0] > 0
