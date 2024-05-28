class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l, r = 0, 0
        curr_sum = 0
        freq_ones = 0
        
        res = 0

        while r < len(nums):
            curr_sum += nums[r]

            if nums[r] == 1:
                freq_ones = 0
            
            if curr_sum > goal:
                curr_sum -= nums[l]
                l += 1
            
            while l <= r and curr_sum == goal:
                curr_sum -= nums[l]
                l += 1
                freq_ones += 1
            
            res += freq_ones

            r += 1
        
        return res
