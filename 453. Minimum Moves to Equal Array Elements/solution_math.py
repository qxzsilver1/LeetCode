class Solution:
    def minMoves(self, nums: list[int]) -> int:
        moves = 0

        min_val = float('inf')

        for num in nums:
            moves += num
            min_val = min(min_val, num)
        
        return moves - min_val * len(nums)
