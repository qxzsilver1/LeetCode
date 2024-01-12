class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = max(nums)
        curr_min, curr_max = 1, 1
        
        for n in nums:
            tmp_curr_max = curr_max
            curr_max = max(n * tmp_curr_max, n * curr_min, n)
            curr_min = min(n * tmp_curr_max, n * curr_min, n)

            output = max(output, curr_max)
        
        return output
