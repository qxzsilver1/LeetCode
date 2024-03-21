class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        zero_ctr = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                res += zero_ctr * (zero_ctr + 1) // 2
                zero_ctr = 0
                continue
            
            if nums[i] == 0:
                zero_ctr += 1

                if i == len(nums) - 1:
                    res += zero_ctr * (zero_ctr + 1) // 2

        return res
