class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        l, r = 0, 0
        res = 0
        curr_prod = 1

        while r < len(nums):
            curr_prod *= nums[r]

            while curr_prod >= k:
                curr_prod //= nums[l]
                l += 1
            
            res += 1 + (r - l)
            r += 1
    
        return res
        
