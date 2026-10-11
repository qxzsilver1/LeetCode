class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)

        res = 0
        i = 1

        while i * i <= n:
            if n % i == 0:
                res += nums[i - 1] * nums[i - 1]

                if i * i != n:
                    res += nums[n // i - 1] ** 2
            i += 1
        
        return res
