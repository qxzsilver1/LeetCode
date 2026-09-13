class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, limit, visited):
            if r == ROWS - 1 and c == COLS - 1:
                return True
            
            visited.add((r, c))

            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc

                if new_r < 0 or new_r == ROWS or new_c < 0 or new_c == COLS or (new_r, new_c) in visited or abs(heights[new_r][new_c] - heights[r][c]) > limit:
                    continue
                
                if dfs(new_r, new_c, limit, visited):
                    return True
            
            return False
        
        l, r = 0, 1000000
        res = r

        while l <= r:
            m = (l + r) // 2

            if dfs(0, 0, m, set()):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
        
        return 0
