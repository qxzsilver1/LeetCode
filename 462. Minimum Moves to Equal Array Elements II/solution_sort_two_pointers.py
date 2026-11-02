class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        res = 0
        l, r = 0, len(nums) - 1
        nums.sort()

        while l < r:
            res += nums[r] - nums[l]

            l += 1
            r -= 1
        
        return res
