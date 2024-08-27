class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max_val, min_val = max(nums), min(nums)
        
        for n in nums:
            if n != max_val and n != min_val:
                return n
        
        return -1
