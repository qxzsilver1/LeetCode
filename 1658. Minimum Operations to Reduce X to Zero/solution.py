class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        running_sum = 0
        l = 0

        max_window = -1

        for r in range(len(nums)):
            running_sum += nums[r]
            
            while l <= r and running_sum > target:
                running_sum -= nums[l]
                l += 1
            
            if running_sum == target:
                max_window = max(max_window, r - l  + 1)

        
        return -1 if max_window == -1 else len(nums) - max_window 
            
