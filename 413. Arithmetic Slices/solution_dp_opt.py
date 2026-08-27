class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = 0

        res = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp = 1 + dp
                res += dp
            else:
                dp = 0
        
        return res
