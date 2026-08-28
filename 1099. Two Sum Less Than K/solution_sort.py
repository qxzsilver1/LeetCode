class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        res = -1
        
        nums.sort()

        for i in range(len(nums)):
            j = bisect_left(nums, k - nums[i], i + 1) - 1
            
            if j > i:
                res = max(res, nums[i] + nums[j])
        
        return res
