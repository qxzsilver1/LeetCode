class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        int_sqrt_n = isqrt(n)
        print(int_sqrt_n)

        res = 0

        for i in range(int_sqrt_n):
            if n % (i + 1):
                continue
            
            res += nums[i] ** 2 + nums[n // (i+1) - 1] ** 2 if i + 1 != n // (i + 1) else nums[i] ** 2
        
        return res
