class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        res = 0
        nums.sort()

        n = len(nums)

        for num in nums:
            res += abs(nums[n // 2] - num)
        
        return res
