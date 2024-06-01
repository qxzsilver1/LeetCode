class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        incr, decr = True, True

        for i in range(len(nums) - 1):
            if not nums[i] <= nums[i+1]:
                incr = False
            if not nums[i] >= nums[i+1]:
                decr = False
        
        return incr or decr
