class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        i = 0

        while i < len(nums):
            zero_ctr = 0

            while i < len(nums) and nums[i] == 0:
                i += 1
                zero_ctr += 1
                res += zero_ctr
            
            i += 1

        return res
