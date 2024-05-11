class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0

        for n in nums:
            tmp = max(n + sum1, sum2)
            sum1 = sum2
            sum2 = tmp
        
        return sum2

