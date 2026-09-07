class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        curr_subarray = 1
        subarray_cnt = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_subarray += 1
            else:
                curr_subarray = 1
            
            subarray_cnt += curr_subarray
        
        return subarray_cnt
