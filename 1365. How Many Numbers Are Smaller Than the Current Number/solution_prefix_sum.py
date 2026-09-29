class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        num_counts = [0] * 101
        prefix_sum = [0] * 101

        for num in nums:
            num_counts[num] += 1
        
        for i in range(1, len(num_counts)):
            prefix_sum[i] = prefix_sum[i - 1] + num_counts[i - 1]
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix_sum[nums[i]] 
        
        return res
