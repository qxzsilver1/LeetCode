class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)

        prefix_sum = 0

        for i in range(len(nums)):
            suffix_sum = nums_sum - (nums[i] + prefix_sum)
            if prefix_sum == suffix_sum:
                return i
            
            prefix_sum += nums[i]
        
        return -1
