class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)

            for curr_sum, cnt in dp.items():
                next_dp[curr_sum + nums[i]] += cnt
                next_dp[curr_sum - nums[i]] += cnt
            
            dp = next_dp
        return dp[target]
