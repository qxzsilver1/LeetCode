class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        m = len(nums) // 2

        mid_elem = nums[m]

        l, r = m, m

        while l > 0 and r < len(nums) - 1:
            l -= 1
            r += 1

            if nums[r] == mid_elem or nums[l] == mid_elem:
                return False
        
        return True
