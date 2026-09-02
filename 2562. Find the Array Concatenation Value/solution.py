class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        concat_val = 0

        while l < r:
            r_len = len(str(nums[r]))
            concat_val += nums[l] * 10 ** r_len + nums[r]
            l += 1
            r -= 1
        
        if l == r:
            concat_val += nums[l]
        
        return concat_val
