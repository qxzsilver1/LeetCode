class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        res = -1
        curr_sum = 0

        for n in nums:
            if curr_sum > n:
                res = curr_sum + n
            
            curr_sum += n
        
        return res
