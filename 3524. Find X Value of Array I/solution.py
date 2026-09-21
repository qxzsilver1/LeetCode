class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        res = [0] * k
        dp = [0] * k

        for i in range(n):
            n_dp = [0] * k

            n_dp[nums[i] % k] += 1

            for r in range(k):
                n_dp[(r * nums[i]) % k] += dp[r]
            
            dp = n_dp

            for r in range(k):
                res[r] += dp[r]
        
        return res
