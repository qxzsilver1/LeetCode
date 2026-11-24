class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 2

        prod_val = 1

        n = len(nums)

        l, r = 0, 0

        while r < n:
            while gcd(prod_val, nums[r]) > 1:
                prod_val //= nums[l]
                l += 1
            
            prod_val *= nums[r]
            res = max(res, r - l + 1)
            r += 1
        
        return res
