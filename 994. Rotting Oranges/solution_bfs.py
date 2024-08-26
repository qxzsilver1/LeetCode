class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        time = 0
        num_fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and num_fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1:
                        continue
                    
                    grid[row][col] = 2
                    q.append((row, col))
                    num_fresh -= 1
                
            time += 1
        
        return time if not num_fresh else -1
