class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        res = -1
        
        nums.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            curr_sum = nums[l] + nums[r]

            if curr_sum < k:
                res = max(res, curr_sum)
                l += 1
            else:
                r -= 1
        
        return res
