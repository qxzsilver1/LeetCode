class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, curr_sum = 0, 0
        prefix_sum_dict = { 0: 1 }

        for n in nums:
            curr_sum += n
            diff = curr_sum - k

            res += prefix_sum_dict.get(diff, 0)
            prefix_sum_dict[curr_sum] = 1 + prefix_sum_dict.get(curr_sum, 0)
        
        return res
