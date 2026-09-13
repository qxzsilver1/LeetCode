class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(limit, visited):

            q = deque([(0, 0)])

            while q:
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return True
                
                visited.add((r, c))
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc

                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visited:
                        curr_diff = abs(heights[new_r][new_c] - heights[r][c])

                        if curr_diff <= limit:
                            visited.add((new_r, new_c))
                            q.append((new_r, new_c))
                    
            
            return False
        
        l, r = 0, 1000000
        res = r

        while l < r:
            m = (l + r) // 2

            if bfs(m, set()):
                r = m
            else:
                l = m + 1
        
        return l
