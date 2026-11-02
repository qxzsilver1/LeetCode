class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        min_val = float('inf')

        for num in nums:
            curr_sum = 0

            for val in nums:
                curr_sum += abs(val - num)
            
            min_val = min(min_val, curr_sum)
        
        return min_val
