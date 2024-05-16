class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] != i:
                if nums[i+1] == i and nums[i] == i + 1:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                else:
                    return False
            
        return True
