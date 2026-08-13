class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def canPlace(num, r, c):
            return not (num in rows[r] or num in cols[c] or num in boxes[box_idx(r, c)])
        
        def placeNumber(num, r, c):
            rows[r][num] += 1
            cols[c][num] += 1
            boxes[box_idx(r, c)][num] += 1
            board[r][c] = str(num)
        
        def removeNumber(num, r, c):
            rows[r][num] -= 1
            cols[c][num] -= 1
            boxes[box_idx(r, c)][num] -= 1

            if rows[r][num] == 0:
                del rows[r][num]
            
            if cols[c][num] == 0:
                del cols[c][num]
            
            if boxes[box_idx(r, c)][num] == 0:
                del boxes[box_idx(r, c)][num]
            
            board[r][c] = '.'
        
        def placeNextNumbers(r, c):
            if c == N - 1 and r == N - 1:
                sudoku_solved[0] = True
            else:
                if c == N - 1:
                    backtrack(r + 1, 0)
                else:
                    backtrack(r, c + 1)
        
        def backtrack(r=0, c=0):
            if board[r][c] == '.':
                for num in range(1, 10):
                    if canPlace(num, r, c):
                        placeNumber(num, r, c)
                        placeNextNumbers(r, c)

                        if sudoku_solved[0]:
                            return
                        
                        removeNumber(num, r, c)
            else:
                placeNextNumbers(r, c)
        
        n = 3
        N = n ** 2

        box_idx = lambda r, c: (r // n) * n + c // n

        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    placeNumber(num, i, j)
        
        sudoku_solved = [False]
        backtrack()
