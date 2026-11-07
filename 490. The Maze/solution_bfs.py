class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]

        q = deque()
        q.append(start)

        visited[start[0]][start[1]] = True
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        while q:
            curr = q.popleft()

            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True
            
            for d in dirs:
                r, c = curr[0], curr[1]
                while 0 <= r < m and 0 <= c < n and maze[r][c] == 0:
                    r += d[0]
                    c += d[1]
                
                r -= d[0]
                c -= d[1]

                if not visited[r][c]:
                    q.append([r, c])
                    visited[r][c] = True
        return False
