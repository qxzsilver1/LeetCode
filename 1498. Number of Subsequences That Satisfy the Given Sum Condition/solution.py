class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0

        r = len(nums) - 1

        for l in range(len(nums)):
            while (nums[l] + nums[r]) > target and l <= r:
                r -= 1
            
            if l <= r:
                res += 2 ** (r - l)

        return res % (10 ** 9 + 7)
