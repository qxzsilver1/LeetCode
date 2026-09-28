class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()

        moves = 0

        for i in range(1, len(nums)):
            diff = (moves + nums[i]) - nums[i - 1]
            nums[i] += moves
            moves += diff
        
        return moves
