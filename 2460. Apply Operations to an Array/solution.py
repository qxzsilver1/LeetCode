class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        l = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        
        return nums
