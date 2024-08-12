class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diags = set() # (r + c) constant
        neg_diags = set() # (r - c) constant

        res = []

        board = [['.'] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                board_copy = [''.join(row) for row in board]
                res.append(board_copy)

                return
            
            for c in range(n):
                if c in cols or (r + c) in pos_diags or (r - c) in neg_diags:
                    continue
                
                cols.add(c)
                pos_diags.add(r + c)
                neg_diags.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                cols.remove(c)
                pos_diags.remove(r + c)
                neg_diags.remove(r - c)
                board[r][c] = '.'
        
        backtrack(0)

        return res
