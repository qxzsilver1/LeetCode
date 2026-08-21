class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1

        for i in range(len(nums)):
            for curr_sum, cnt in dp[i].items():
                dp[i+1][curr_sum + nums[i]] += cnt
                dp[i+1][curr_sum - nums[i]] += cnt

        return dp[len(nums)][target]
