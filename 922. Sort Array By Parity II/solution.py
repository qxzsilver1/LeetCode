class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < len(nums) and r > 0:
            if not nums[l] % 2:
                l += 2
            elif nums[r] % 2:
                r -= 2
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 2
                r -= 2
        
        return nums
