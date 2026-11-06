class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c):
            if visited[r][c]:
                return False
            
            if r == destination[0] and c == destination[1]:
                return True

            visited[r][c] = True
            dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

            for d in dirs:
                r_new = r
                c_new = c
                # Move the ball in the chosen direction until it can.
                while 0 <= r_new < m and 0 <= c_new < n and maze[r_new][c_new] == 0:
                    r_new += d[0]
                    c_new += d[1]
                # Revert the last move to get the cell to which the ball rolls.
                if dfs(r_new - d[0], c_new - d[1]):
                    return True
            return False
        
        return dfs(start[0], start[1])
