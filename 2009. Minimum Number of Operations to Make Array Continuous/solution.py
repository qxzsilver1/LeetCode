class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n_len = len(nums)
        nums = sorted(set(nums))

        res = n_len

        r = 0
        for l in range(len(nums)):
            while r < len(nums) and nums[r] < nums[l] + n_len:
                r += 1

            window = r - l
            res = min(res, n_len - window)
        
        return res
