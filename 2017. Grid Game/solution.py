class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        prefix_row1, prefix_row2 = [0] * n, [0] * n

        for i in range(n):
            prefix_row1[i] = prefix_row1[i-1] + grid[0][i] if i > 0 else grid[0][0]
            prefix_row2[i] = prefix_row2[i-1] + grid[1][i] if i > 0 else grid[1][0]
        
        res = float('inf')

        for i in range(n):
            top_row = prefix_row1[-1] - prefix_row1[i]
            bottom_row = prefix_row2[i-1] if i > 0 else 0

            second_robot = max(top_row, bottom_row)

            res = min(res, second_robot)
        
        return res
