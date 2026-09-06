class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        m = len(nums) // 2

        mid_elem = nums[m]

        for i in range(len(nums)):
            if i != m and nums[i] == mid_elem:
                return False
        
        return True
