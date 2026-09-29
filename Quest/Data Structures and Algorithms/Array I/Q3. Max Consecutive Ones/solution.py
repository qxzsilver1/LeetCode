class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        i = 1

        while i < len(nums):
            nums[i] += nums[i - 1] * nums[i]
            nums[0] = nums[0] ^ ((nums[0] ^ nums[i]) & -(nums[0] < nums[i]))
            i += 1

        return nums[0]
