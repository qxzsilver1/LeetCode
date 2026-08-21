class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        possible_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        chessboard = [[0] * n for _ in range(m)]
        chessboard[r][c] = -1

        def isValidMove(to_row, to_col):
            return 0 <= to_row < m and 0 <= to_col < n and chessboard[to_row][to_col] == 0
        
        def solveKnightsTour(curr_row, curr_col, move_cnt):
            if move_cnt == m * n:
                return True
            
            for dr, dc in possible_moves:
                n_r, n_c = curr_row + dr, curr_col + dc

                if isValidMove(n_r, n_c):
                    chessboard[n_r][n_c] = move_cnt

                    if solveKnightsTour(n_r, n_c, move_cnt + 1):
                        return True
                    
                    chessboard[n_r][n_c] = 0
            
            return False
        
        solveKnightsTour(r, c, 1)

        chessboard[r][c] = 0

        return chessboard
        
