class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        board.reverse()

        def intToCoord(square_num):
            r = (square_num - 1) // n
            c = (square_num - 1) % n

            if r % 2:
                c = n - 1 - c

            return (r, c)

        q = deque() # (square, moves)
        q.append((1, 0))

        visited = set()

        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                next_square = square + i
                r, c = intToCoord(next_square)

                if board[r][c] != -1:
                    next_square = board[r][c]
                
                if next_square == n * n:
                    return moves + 1
                
                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))
        
        return -1
