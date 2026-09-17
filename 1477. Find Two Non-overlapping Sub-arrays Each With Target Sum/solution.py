class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        res = n + 1

        curr_sum = 0

        dp = [n] * (n + 1)
        l = 0

        for r, x in enumerate(arr):
            curr_sum += x

            while curr_sum > target:
                curr_sum -= arr[l]
                l += 1
            
            dp[r + 1] = dp[r]

            if curr_sum == target:
                res = min(res, r - l + 1 + dp[l])
                dp[r + 1] = min(dp[r], r - l + 1)
        
        return -1 if res == n + 1 else res
