class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0

        while r < len(nums):
            if nums[l] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            
            r += 1
        
        return l
