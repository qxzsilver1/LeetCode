class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        possible_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        chessboard = [[0] * n for _ in range(m)]
        chessboard[r][c] = -1

        def isValidMove(to_row, to_col):
            return 0 <= to_row < m and 0 <= to_col < n and chessboard[to_row][to_col] == 0
        
        def getNextMovesWarnsdorff(row, col):
            next_moves = []

            for i in range(8):
                n_r, n_c = row + possible_moves[i][0], col + possible_moves[i][1]
                accessibility_score = sum(isValidMove(n_r + move[0], n_c + move[1]) for move in possible_moves)
                next_moves.append((accessibility_score, i))
            
            return sorted(next_moves)
        
        def solveKnightsTour(curr_row, curr_col, move_cnt):
            if move_cnt == m * n:
                return True
            
            next_moves = getNextMovesWarnsdorff(curr_row, curr_col)
            
            for _, move_idx in next_moves:
                n_r, n_c = curr_row + possible_moves[move_idx][0], curr_col + possible_moves[move_idx][1]

                if not isValidMove(n_r, n_c):
                    continue
                
                chessboard[n_r][n_c] = move_cnt

                if solveKnightsTour(n_r, n_c, move_cnt + 1):
                    return True
                    
                chessboard[n_r][n_c] = 0
            
            return False
        
        solveKnightsTour(r, c, 1)

        chessboard[r][c] = 0

        return chessboard
        
