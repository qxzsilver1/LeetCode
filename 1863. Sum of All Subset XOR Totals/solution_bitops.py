class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res |= n
        
        # return res * 2 ** (len(nums) - 1)
        return res << (len(nums) - 1)
