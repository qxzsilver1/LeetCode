class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        zero_ctr = 0

        for n in nums:
            if n == 0:
                zero_ctr += 1
                res += zero_ctr
            else:
                zero_ctr = 0
                continue

        return res
