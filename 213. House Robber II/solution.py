class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)

        def house_robber(nums):
            sum1, sum2 = 0, 0
            for n in nums:
                tmp = max(n + sum1, sum2)
                sum1 = sum2
                sum2 = tmp
            
            return sum2
        
        return max(nums[0], house_robber(nums[:l-1]), house_robber(nums[1:]))
