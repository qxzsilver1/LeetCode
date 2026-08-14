class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        rows = len(board)
        cols = len(board[0])

        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        def countMines(r, c):
            count = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            
            return count
        
        def reveal(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'E':
                return

            mines = countMines(r, c)

            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'

                for dr, dc in dirs:
                    reveal(r + dr, c + dc)
        
        reveal(r, c)

        return board
