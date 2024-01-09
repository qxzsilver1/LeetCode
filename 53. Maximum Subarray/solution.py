class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            
            curr_sum += n
            max_subarray = max(max_subarray, curr_sum)
        
        return max_subarray
