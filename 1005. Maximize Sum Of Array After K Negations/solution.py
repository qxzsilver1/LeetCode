class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        neg_counter = 0
        n = len(nums)

        for i in range(k):
            idx = nums.index(min(nums))
            nums[idx] = - nums[idx]
        
        return sum(nums)
