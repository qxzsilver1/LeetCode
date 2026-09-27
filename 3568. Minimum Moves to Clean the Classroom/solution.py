class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        m, n = len(classroom), len(classroom[0])

        grid = [[0] * n for _ in range(m)]

        start_x, start_y = 0, 0
        cnt = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start_x, start_y = i, j
                elif classroom[i][j] == 'L':
                    grid[i][j] = 1 << cnt
                    cnt += 1
        
        full_mask = 1 << cnt

        best_energy = [[[-1 for _ in range(full_mask)] for _ in range(n)] for _ in range(m)]
        best_energy[start_x][start_y][0] = energy

        curr_stats = deque()
        curr_stats.append((start_x, start_y, 0, energy, 0))

        while curr_stats:
            x, y, mask, e, steps = curr_stats.popleft()

            if mask == full_mask - 1:
                return steps
            
            if e == 0:
                continue
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx == m or ny < 0 or ny == n or classroom[nx][ny] == 'X':
                    continue
                
                n_energy = energy if classroom[nx][ny] == 'R' else e - 1
                n_mask = mask | grid[nx][ny]

                if n_energy > best_energy[nx][ny][n_mask]:
                    best_energy[nx][ny][n_mask] = n_energy
                    curr_stats.append((nx, ny, n_mask, n_energy, steps + 1))
        
        return -1
