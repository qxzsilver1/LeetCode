class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        
        for k in range(1, 4):
            for i in range(n - k):
                if nums[i] == nums[i + k]:
                    return nums[i]
