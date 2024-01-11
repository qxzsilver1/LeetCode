class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        sum_tot = n * (n+1) // 2

        for n in nums:
            sum_tot -= n
        
        return -sum_tot
