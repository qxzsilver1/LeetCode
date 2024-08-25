class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0

        for r in range(len(nums)):
            if not nums[r] % 2:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return nums
