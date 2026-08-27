class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        
        indegrees = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] < matrix[r][c]:
                        indegrees[r][c] += 1
        
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if indegrees[r][c] == 0:
                    q.append([r, c])
        
        longest_incr_subseq = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                        indegrees[nr][nc] -= 1
                        
                        if indegrees[nr][nc] == 0:
                            q.append([nr, nc])
            
            longest_incr_subseq += 1
        
        return longest_incr_subseq
