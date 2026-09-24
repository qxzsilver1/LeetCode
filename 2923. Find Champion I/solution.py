class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        max_score = 0
        max_idx = -1

        for i in range(n):
            curr_score = sum(grid[i])

            if curr_score > max_score:
                max_score = curr_score
                max_idx = i
        
        return max_idx
