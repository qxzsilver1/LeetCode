class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        num_ones_over_zeroes = 0

        res = 0

        ones_difference_index = {}

        for i, n in enumerate(nums):
            if n == 0:
                num_ones_over_zeroes -= 1
            else:
                num_ones_over_zeroes += 1
            
            if num_ones_over_zeroes not in ones_difference_index:
                ones_difference_index[num_ones_over_zeroes] = i
            
            if not num_ones_over_zeroes:
                res = i + 1
            else:
                idx = ones_difference_index[num_ones_over_zeroes]
                res = max(res, i - idx)
            
        return res
