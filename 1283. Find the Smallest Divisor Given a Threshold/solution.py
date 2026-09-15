class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        res = -1
        l, r = 1, max(nums)

        def divisionSum(divisor):
            ans = 0

            for num in nums:
                ans += ceil((num * 1.0) / divisor)
            
            return ans
        
        while l <= r:
            m = (l + r) // 2
            div_sum = divisionSum(m)

            if div_sum <= threshold:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
