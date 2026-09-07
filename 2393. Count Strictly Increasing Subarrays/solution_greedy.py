class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        subarray_cnt = 0

        i = 0

        while i < len(nums):
            curr_subarray = 1

            while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                curr_subarray += 1
                i += 1
            
            i += 1
            
            subarray_cnt += (curr_subarray * (curr_subarray + 1)) // 2
        
        return subarray_cnt
